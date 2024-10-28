
from django import forms
from display.models import BillingAddress, ShippingAddress



class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)






class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['street_address']
     



class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['street_address']
       
