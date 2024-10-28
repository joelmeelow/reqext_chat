from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from home.models import pharmauser

class ChatMessage(models.Model):
    group_name = models.CharField(max_length=255)
    message = models.TextField()
    pharmacist = models.ForeignKey(pharmauser, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class MedicalCondition(models.Model):
    condition = models.CharField(max_length=255)
    symptoms = models.TextField()
    question = models.TextField()
    answer = models.TextField()
    picture_url = models.URLField(blank=True, null=True)
