# admin.py

from django.contrib import admin
from .models import (
    Items,
    ProductRatingReview,
    Review,
    Bonus,
    MostSearched,
    History,
    OrderItems,
    Order,
    ShippingAddress,
    BillingAddress,
)

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_entered', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category', 'date_entered')

@admin.register(ProductRatingReview)
class ProductRatingReviewAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'name', 'number_stars', 'date_created')
    search_fields = ('product_name__name', 'name__email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_name', 'date')
    search_fields = ('product_name__name', 'name__email')
    list_filter = ('date',)

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('name', 'bonuses', 'date_gained')
    search_fields = ('name__email',)

@admin.register(MostSearched)
class MostSearchedAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'date')
    search_fields = ('product__name',)

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'date_sold')
    search_fields = ('product__name',)

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'total_price', 'user', 'ordered')
    search_fields = ('item__name', 'user__email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'ordered', 'total_price')
    search_fields = ('user__email',)
    list_filter = ('ordered', 'order_date')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'country', 'default')
    search_fields = ('user__email',)

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'country', 'default')
    search_fields = ('user__email',)

