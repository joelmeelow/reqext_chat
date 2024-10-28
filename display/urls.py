from django.urls import path
from . import views
from .views import OrderSummaryView, DisplayProductView, DisplayProductView

app_name = 'display'

urlpatterns = [
    path('', views.main, name="index"),

    path('product/<slug:slug>/', DisplayProductView.as_view(), name='single_product'),
    path('addtocart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('removefromcart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('removesingle/<slug:slug>/', views.remove_single_item_from_cart, name='remove_single_item'),
    path('addsinglecart/<slug:slug>/', views.add_a_single_item_to_cart, name='add_single_item'),
    path('ordersummary/', OrderSummaryView.as_view(), name='order_summary'),
    path('getreview/<slug:slug>/', views.get_reviews, name='get_review'),
    path('checkquantity/<str:pk>/', views.update_count, name="check_quantity"),
]
