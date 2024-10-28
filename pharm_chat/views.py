from django.shortcuts import render, get_object_or_404
from home.models import pharmauser, PharmacistClicked
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)

@login_required
def patient_list(request):
    user_id = request.user.id
    patients = PharmaUser.objects.filter(chat_messages__pharmacist__id=user_id).distinct()

    patient_data = []
    for patient in patients:
        unread_count = ChatMessage.objects.filter(
            group_name=f"{patient.name}_{user_id}", is_read=False).count()
        patient_data.append({
            'id': patient.id,
            'name': patient.name,
            'unread_count': unread_count,
        })

    context = {
        'patients': patient_data,
    }
    return render(request, 'pharm_chat/patient_list.html', context)

def pharma_chat(request, username):
    if request.method == 'GET':
        pharmacist = get_object_or_404(pharmauser, name=username)
        user_id = request.user.id
        user_name = request.user.username
        group_name = f"{pharmacist.name}_{user_id}"
        PharmacistClicked.increment_click_count(pharmacist, request.user)
        # Retrieve messages related to this group
        group_messages = ChatMessage.objects.filter(group_name=group_name).order_by('timestamp')
        unread_count = group_messages.filter(is_read=False).count()

        context = {
            'user_name': user_name,
            'user_id': user_id,
            'username': username,
            'pharmacist': pharmacist,
            'group_name': group_name,
            'group_messages': group_messages,
            'unread_count': unread_count,
        }

        return render(request, 'pharm_chat/chat3.html', context)

@login_required
def mark_messages_as_read(request, patient_id):
    if request.method == 'POST':
        patient_user = get_object_or_404(PharmaUser, id=patient_id)
        pharmacist_id = request.user.id
        group_name = f"{patient_user.name}_{pharmacist_id}"

        # Mark messages as read
        ChatMessage.objects.filter(group_name=group_name, is_read=False).update(is_read=True)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@login_required
def generate_questions(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            symptoms = data.get('symptoms')
            previous_answers = data.get('answers', [])
            picture_url = data.get('picture_url')
            pharmacist_name = data.get('pharmacist_name')

            # Input validation
            if not symptoms or not isinstance(symptoms, str):
                return JsonResponse({'status': 'error', 'message': 'Invalid symptoms provided'}, status=400)
            if previous_answers and not isinstance(previous_answers, list):
                return JsonResponse({'status': 'error', 'message': 'Invalid answers format'}, status=400)

            # Rate limiting
            user_cache_key = f"generate_questions_{request.user.id}"
            if cache.get(user_cache_key):
                return JsonResponse({'status': 'error', 'message': 'Rate limit exceeded. Please wait.'}, status=429)
            cache.set(user_cache_key, True, timeout=10)

            # Construct the prompt
            prompt = f"Generate a list of questions based on these symptoms: {symptoms}."
            if picture_url:
                prompt += f" Also consider the provided image: {picture_url}."
            if previous_answers:
                prompt += f" The patient's previous answers were: {', '.join(previous_answers)}."

            # Generate questions
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            questions = response.choices[0].message['content'].strip().split('\n')

            # Save symptom history
            pharmacist = PharmaUser.objects.get(name=pharmacist_name)
            symptom_history = SymptomHistory.objects.create(
                patient=request.user,
                pharmacist=pharmacist,
                symptoms=symptoms,
                picture=picture_url,
                questions_generated=questions,
                answers=[],  # Initialize empty list for answers
                suggested_diagnosis="",
            )

            return JsonResponse({'status': 'success', 'questions': questions, 'history_id': symptom_history.id})

        except Exception as e:
            logger.error(f"Error generating questions for user {request.user.id}: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred while generating questions.'}, status=500)

@login_required
def diagnose_condition(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            history_id = data.get('history_id')
            answers = data.get('answers')
            picture_url = data.get('picture_url')

            symptom_history = get_object_or_404(SymptomHistory, id=history_id)
            symptoms = symptom_history.symptoms

            # Construct the prompt for diagnosis
            prompt = f"Given the symptoms: {symptoms}, and the patient's answers: {answers}, what are the possible medical diagnoses?"
            if picture_url:
                prompt += f" Also consider the provided image: {picture_url}."

            # Generate possible diagnoses
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            diagnoses = response.choices[0].message['content'].strip().split('\n')

            # Update suggested diagnosis in the SymptomHistory
            symptom_history.suggested_diagnosis = '\n'.join(diagnoses)
            symptom_history.answers = answers  # Save answers
            symptom_history.save()

            return JsonResponse({'status': 'success', 'diagnoses': diagnoses})

        except Exception as e:
            logger.error(f"Error diagnosing condition for user {request.user.id}: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred while diagnosing.'}, status=500)

@csrf_exempt
@login_required
def submit_final_diagnosis(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        final_diagnosis = data.get('diagnosis')
        history_id = data.get('history_id')

        try:
            symptom_history = get_object_or_404(SymptomHistory, id=history_id)
            symptom_history.final_diagnosis = final_diagnosis
            symptom_history.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.error(f"Error submitting final diagnosis for user {request.user.id}: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred while submitting the final diagnosis.'}, status=500)
