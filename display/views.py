import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Items, Order, OrderItems, Bonus, Review
from home.models import PharmacistClicked

class GeneralDisplayView(ListView):
    model = Items
    template_name = 'display/general_display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItems.objects.all()
        context['pharmacistcount'] = PharmacistClicked.countobjects.with_counts()
        return context


class DisplayProductView(DetailView):
    model = Items
    context_object_name = 'product'  # Singular for clarity
    template_name = 'display/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def main(request):
    """Display the main page with all items."""
    items = Items.objects.all()
    order_items = OrderItems.objects.all()
    bonus = Bonus.objects.all()
    context = {
        'items': items,
        'order_items': order_items,
        'bonus': bonus
    }
    return render(request, 'display/main.html', context)


@login_required
def update_count(request, pk):
    """Update item count in the user's cart."""
    if request.method == 'GET':
        item = get_object_or_404(Items, pk=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs.first()
            order_item = order.items.filter(item=item).first()
            if order_item:
                data = {"quantity": order_item.quantity}
                return JsonResponse(data=data, status=200)
        return JsonResponse({"message": "Item not found."}, status=404)
    return JsonResponse({"message": "Send a GET request."}, status=400)


@login_required
def add_to_cart(request, slug):
    """Add an item to the user's cart."""
    item = get_object_or_404(Items, slug=slug)
    order_item, created = OrderItems.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
        defaults={'total_price': item.price}
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        if order.items.filter(item=order_item.item).exists():
            if order_item.item.quantity > order_item.quantity:
                order_item.quantity += 1
                order_item.total_price = item.price * order_item.quantity
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                messages.info(request, 'The quantity you entered exceeds available stock.')
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
    else:
        order = Order.objects.create(user=request.user, ordered_date=datetime.datetime.now())
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")

    return redirect("core:order-summary")


@login_required
def remove_from_cart(request, slug):
    """Remove an item from the user's cart."""
    item = get_object_or_404(Items, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        order_item = order.items.filter(item=item).first()
        if order_item:
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        messages.info(request, "This item was not in your cart.")
    else:
        messages.info(request, "You do not have an active order.")
    return redirect("core:product", slug=slug)


@login_required
def modify_cart_item(request, slug, increment=True):
    """Helper function to modify item quantity in the cart."""
    item = get_object_or_404(Items, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        order_item = order.items.filter(item=item).first()
        if order_item:
            if increment:
                if order_item.quantity < order_item.item.quantity:
                    order_item.quantity += 1
                    messages.info(request, "This item quantity was updated.")
                else:
                    messages.info(request, f"The available stock is {order_item.item.quantity}.")
            else:
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    messages.info(request, "This item quantity was updated.")
                else:
                    order.items.remove(order_item)
                    order_item.delete()
                    messages.info(request, "This item was removed from your cart.")
            order_item.save()
        else:
            messages.info(request, "This item was not in your cart.")
    else:
        messages.info(request, "You do not have an active order.")
    return redirect("core:product", slug=slug)


@login_required
def add_a_single_item_to_cart(request, slug):
    """Add a single item to the cart."""
    return modify_cart_item(request, slug, increment=True)


@login_required
def remove_single_item_from_cart(request, slug):
    """Remove a single item from the cart."""
    return modify_cart_item(request, slug, increment=False)


@login_required
def get_reviews(request, pk):
    """Handle adding reviews for products."""
    product = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        review_text = request.POST.get('review')
        if review_text:
            Review.objects.create(name=request.user, product_name=product, reviews=review_text)
            messages.success(request, "Review added successfully.")
            return redirect('core:product', slug=product.slug)
    return render(request, 'reviews.html', {'product': product})


class OrderSummaryView(View):
    """Display the user's order summary."""
    @login_required
    def get(self, *args, **kwargs):
        try:
            user = self.request.user
            order = Order.objects.get(user=user, ordered=False)
            totals = get_total_price(user)  # Ensure this function is defined
            context = {
                'object': order,
                'totals': totals
            }
            return render(self.request, 'order_summary.html', context)
        except Order.DoesNotExist:
            messages.warning(self.request, "You do not have an active order.")
            return redirect("/")
