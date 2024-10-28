
from django.urls import path
from .views import CheckoutView, PaymentView, BillingView, ShippingView
from . import views


app_name = 'payment'

urlpatterns = [
    #path('', views.index, name="index"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
   
    path('billingview/', BillingView.as_view(), name="billing"),
   
    path('shippingview/', ShippingView.as_view(), name='shipping'),
    path('gethistory/', views.get_history, name='gethistory' ),
    path('paymentview/', PaymentView.as_view(), name='paymentview')
   
]
