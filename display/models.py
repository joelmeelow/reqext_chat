from datetime import date
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django_countries.fields import CountryField
from payment.models import Payment
from django.db.models import F, Sum


# Custom QuerySet for filtering items with quantities greater than 0
class ProductQuery(models.QuerySet):
    def check_quantity(self):
        return self.filter(quantity__gt=0)


class Items(models.Model):
    CATEGORY_CHOICES = [
        ('sexual health', 'Sexual Health'),
        ('skin health', 'Skin Health'),
        ('immune system', 'Immune System'),
        # Add other categories as needed
    ]
    
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    date_entered = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    objects = ProductQuery.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('display:singleproduct', kwargs={'slug': self.slug})


def product_count_increment(item, user):
    count, created = ProductsClicked.objects.get_or_create(item=item, client=user)
    if not created:
        count.count = F('count') + 1
        count.save()


class ProductRatingReview(models.Model):
    product_name = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='ratings')
    number_stars = models.IntegerField(null=True, blank=True, verbose_name='Number of Stars')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    date_created = models.DateField(editable=False, default=timezone.now)
    product_review = models.CharField(max_length=3000, verbose_name='Product Review', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        super().save(*args, **kwargs)


class Review(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User Review')
    product_name = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='reviews', verbose_name='Product Name')
    reviews = models.CharField(max_length=300, null=True, blank=True, verbose_name='User Review')
    date = models.DateField()

    class Meta:
        ordering = ['date']


class Bonus(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client with Bonus')
    bonuses = models.IntegerField(default=0)
    date_gained = models.DateField(default=timezone.now)

    # Additional logic can be added here for bonus management


class MostSearched(models.Model):
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    # Logic for updating this model on product clicks


class History(models.Model):
    product = models.ManyToManyField(Items)
    quantity = models.IntegerField(default=0)
    date_sold = models.DateField(default=timezone.now)

    # Logic for updating history on completed orders


class OrderItems(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Item Ordered')
    quantity = models.IntegerField(default=1, verbose_name='Ordered Quantity')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Price')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_items', verbose_name='User Ordering')
    ordered = models.BooleanField(default=False)

    def get_purchase_discount(self):
        # Logic for calculating purchase discounts
        pass


def get_total_price(user):
    order = Order.objects.filter(user=user, ordered=False).first()
    if order:
        total_price = sum(item.total_price for item in order.items.all())
        total_quantity = sum(item.quantity for item in order.items.all())
        return {'price': total_price, 'quantity': total_quantity}
    return {'price': 0, 'quantity': 0}


class Order(models.Model):
    items = models.ManyToManyField(OrderItems)
    order_date = models.DateField(verbose_name='Order Date', default=timezone.now)
    ordered = models.BooleanField(default=False, verbose_name='Ordered')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    loyalty_discount = models.CharField(max_length=100, verbose_name='Loyalty Discount', blank=True, null=True)
    shipping_address = models.ForeignKey('ShippingAddress', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey('BillingAddress', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    saved_address = models.BooleanField(default=False)


class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100, blank=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100, blank=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
