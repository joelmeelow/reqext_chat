from django.urls import path
from .views import (
    patient_list,
    pharma_chat,
    mark_messages_as_read,
    generate_questions,
    diagnose_condition,
    submit_final_diagnosis,
)

app_name = 'pharm_chat'

urlpatterns = [
    path('patients/', patient_list, name='patient_list'),
    path('chat/<str:username>/', pharma_chat, name='pharma_chat'),
    path('mark-messages-as-read/<int:patient_id>/', mark_messages_as_read, name='mark_messages_as_read'),
    path('generate-questions/', generate_questions, name='generate_questions'),
    path('diagnose-condition/', diagnose_condition, name='diagnose_condition'),
    path('submit-final-diagnosis/', submit_final_diagnosis, name='submit_final_diagnosis'),
]
