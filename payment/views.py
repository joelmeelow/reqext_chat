from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
import stripe
from .forms import PaymentForm, BillingAddressForm, ShippingAddressForm
from display.models import Payment, Order, OrderItems, BillingAddress, ShippingAddress
from home.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

class CheckoutView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        order_items = OrderItems.objects.filter(user=user, ordered=False)

        if not order_items.exists():
            messages.info(self.request, "You do not have an active order.")
            return redirect("core:checkout")

        order = order_items.first().order
        form_billing = BillingAddressForm()
        form_shipping = ShippingAddressForm()
        form_payment = PaymentForm()

        shipping_address_qs = ShippingAddress.objects.filter(user=user, default=True)
        billing_address_qs = BillingAddress.objects.filter(user=user, default=True)

        context = {
            'form_billing': form_billing,
            'form_shipping': form_shipping,
            'form_payment': form_payment,
            'order': order,
            'default_shipping_address': shipping_address_qs.first(),
            'default_billing_address': billing_address_qs.first(),
        }

        totals = get_total_price(user)
        context.update(totals)

        return render(self.request, "checkout.html", context)


class BillingView(View):
    def post(self, request):
        if request.method == 'POST':
            order_items = OrderItems.objects.filter(user=request.user, ordered=False)

            if not order_items.exists():
                messages.error(request, "You do not have an active order.")
                return redirect("core:checkout")

            form = BillingAddressForm(request.POST)

            if form.is_valid():
                BillingAddress.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'street_address': form.cleaned_data['street_address'],
                        'apartment_address': form.cleaned_data['apartment_address'],
                        'country': form.cleaned_data['country'],
                        'zip': form.cleaned_data['zip'],
                    }
                )
                messages.success(request, "Billing address updated!")
                return redirect("core:checkout")
            else:
                messages.error(request, "Please correct the errors in the form.")
        return redirect("core:checkout")


class ShippingView(View):
    def post(self, request):
        if request.method == 'POST':
            order_items = OrderItems.objects.filter(user=request.user, ordered=False)

            if not order_items.exists():
                messages.error(request, "You do not have an active order.")
                return redirect("core:checkout")

            form = ShippingAddressForm(request.POST)

            if form.is_valid():
                ShippingAddress.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'street_address': form.cleaned_data['street_address'],
                        'apartment_address': form.cleaned_data['apartment_address'],
                        'country': form.cleaned_data['country'],
                        'zip': form.cleaned_data['zip'],
                    }
                )
                messages.success(request, "Shipping address updated!")
                return redirect("core:checkout")
            else:
                messages.error(request, "Please correct the errors in the form.")
        return redirect("core:checkout")


class PaymentView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        order_items = OrderItems.objects.filter(user=user, ordered=False)

        if not order_items.exists():
            messages.warning(self.request, "You do not have an active order.")
            return redirect("core:checkout")

        order = order_items.first().order
        if order.billing_address:
            context = {
                'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            }
            userprofile = user.userprofile
            if userprofile.one_click_purchasing:
                cards = stripe.Customer.list_sources(userprofile.stripe_customer_id, limit=3, object='card')
                context['card'] = cards['data'][0] if cards['data'] else None
            return render(self.request, "payment.html", context)
        else:
            messages.warning(self.request, "You have not added a billing address.")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        order_items = OrderItems.objects.filter(user=self.request.user, ordered=False)

        if not order_items.exists():
            messages.error(self.request, "You do not have an active order.")
            return redirect("core:checkout")

        order = order_items.first().order
        form = PaymentForm(self.request.POST)
        userprofile = UserProfile.objects.get(user=self.request.user)

        if form.is_valid():
            token = form.cleaned_data.get('stripeToken')
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')

            try:
                if save:
                    if userprofile.stripe_customer_id:
                        customer = stripe.Customer.retrieve(userprofile.stripe_customer_id)
                        customer.sources.create(source=token)
                    else:
                        customer = stripe.Customer.create(email=self.request.user.email)
                        customer.sources.create(source=token)
                        userprofile.stripe_customer_id = customer['id']
                        userprofile.one_click_purchasing = True
                        userprofile.save()

                amount = int(order.total_price * 100)  # Total price in cents
                if use_default or save:
                    charge = stripe.Charge.create(amount=amount, currency="usd", customer=userprofile.stripe_customer_id)
                else:
                    charge = stripe.Charge.create(amount=amount, currency="usd", source=token)

                payment = Payment.objects.create(
                    stripe_charge_id=charge['id'],
                    user=self.request.user,
                    amount=order.total_price
                )

                order.ordered = True
                order.payment = payment
                order.save()

                messages.success(self.request, "Your order was successful!")
                return redirect("home:index")
            except stripe.error.StripeError as e:
                messages.warning(self.request, f"Stripe error: {str(e)}")
                return redirect("/payment/stripe/")
            except Exception as e:
                messages.error(self.request, "An error occurred. Please try again.")
                return redirect("/payment/stripe/")

        messages.warning(self.request, "Invalid data received.")
        return redirect("/payment/stripe/")


def get_history(request):
    user = request.user
    orders = Order.objects.filter(user=user, ordered=True).order_by('-order_date')
    context = {
        'orders': orders
    }
    return render(request, "order_history.html", context)
