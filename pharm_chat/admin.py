from django.contrib import admin
from .models import ChatMessage, MedicalCondition

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'pharmacist', 'patient', 'timestamp', 'is_read')
    search_fields = ('group_name', 'message', 'pharmacist__username', 'patient__username')
    list_filter = ('is_read', 'timestamp')

@admin.register(MedicalCondition)
class MedicalConditionAdmin(admin.ModelAdmin):
    list_display = ('condition', 'symptoms', 'question', 'answer')
    search_fields = ('condition',)
