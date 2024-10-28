from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'timestamp')
    search_fields = ('user__username',)

admin.site.register(Payment, PaymentAdmin)
