
from django.urls import path
from . import views
from .views import GeneralDisplayView, ProductsView, PharmacistView, AllProductsView


app_name = 'home'

urlpatterns = [
    path('', GeneralDisplayView.as_view(), name="index"),
    path('signup/', views.signupview, name="signup"),
    path('products/', ProductsView.as_view(), name='products'),
    path('pharmacists/', PharmacistView.as_view(), name='pharmacists' ),
    path('product/<str:pk>/', views.single_product_view, name='singleproduct'),
    path('uploadimage/<int:pk>/', views.uploadimage, name='uploadimage'),
    path('logout', views.logoutview, name="logout"),
    path('allproduct/', AllProductsView.as_view(), name='allproduct'),
    path('login/', views.signinview, name='login'),
    path('pharmsignup/', views.pharmsignupview, name='pharmsignup' )
   
]

