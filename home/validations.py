from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib import messages

UserModel = get_user_model()

def custom_validation(request, data):
    email = data.get('email', '').strip()  # Use .get() for safety
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    # Check for email validity
    if not email or UserModel.objects.filter(email=email).exists():
        messages.error(request, 'Choose another email')

    # Check for password validity
    if not password or len(password) < 8:
        messages.error(request, 'Choose another password, min 8 characters')

    # Check for username validity
    if not username or len(username) < 8:
        messages.error(request, 'Choose another username, min 8 letters')

    # Return None if there are any error messages
    if messages.get_messages(request):
        return None  # Indicate validation failure

    return data


def validate_email(request, data):
    email = data.get('email', '')  # Use .get() for safety
    if not email:
        messages.error(request, 'An email is needed')
        return False  # Indicate validation failure
    return True


def validate_username(request, data):
    username = data.get('username', '').strip()  # Use .get() for safety
    if not username:
        messages.error(request, 'Choose another username')
        return False  # Indicate validation failure
    return True


def validate_password(request, data):
    password = data.get('password', '').strip()  # Use .get() for safety
    if not password:
        messages.error(request, 'A password is needed')
        return False  # Indicate validation failure
    return True


def validate_pharmacist(request, data):
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    specialization = data.get('specialization', '').strip()
    experience = data.get('experience', '').strip()
    title = data.get('title', '').strip()

    # Validate experience input
    try:
        experience_value = int(experience)
        if experience_value <= 0 or experience_value > 60:
            messages.error(request, 'Please enter a valid experience value (1-60 years)')
    except ValueError:
        messages.error(request, 'Experience must be a number')

    # Check specialization length
    if len(specialization) > 100:
        messages.error(request, 'Please keep it within 100 letters, thank you')

    # Validate title
    if title.lower() != 'pharmacist':
        messages.error(request, 'You must be a pharmacist to register here')

    # Check for required fields
    if not password:
        messages.error(request, 'A password is needed')
    if not email:
        messages.error(request, 'An email is needed')

    # Return None if there are any error messages
    if messages.get_messages(request):
        return None  # Indicate validation failure

    return data
