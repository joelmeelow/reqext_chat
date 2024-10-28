# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import ListView
from display.models import Items, OrderItems
from .forms import ImageForm
from .models import pharmauser, PharmacistClicked
from .validations import custom_validation, validate_email, validate_password, validate_username, validate_pharmacist
from django.contrib.auth import get_user_model

usermodel = get_user_model()

class GeneralDisplayView(ListView):
    model = Items
    template_name = 'home/index.html'
    context_object_name = 'myproduct'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItems.objects.all()
        context['pharmacistcount'] = PharmacistClicked.objects.with_counts()
        context['pharmauser'] = pharmauser.objects.all()
        return context









class ProductsView(ListView):
    template_name = 'home/products.html'
    context_object_name = 'products'
    queryset = Items.objects.all()[:20]



class AllProductsView(ListView):
    template_name = 'home/allproducts.html'
    context_object_name = 'product'
    queryset = Items.objects.all()[:20]


def single_product_view(request, slug):
    products = Items.objects.get(slug=slug)
    similar_products = Items.objects.filter(category=products.category)
    productsclicked, created = ProductsClicked.objects.get_or_create(item=products, client=request.user, count=1)
    
    if not created:
        productsclicked.count += 1
        productsclicked.save()

    bestseller = Order.objects.all()[:10]
    context = {
        'products': products,
        'similar_products': similar_products,
        'productsclicked': productsclicked,
        'bestseller': bestseller
    }
    return render(request, 'home/products.html', context)


from django.views.generic import ListView
from django.http import Http404
from .models import pharmauser, PharmacistClicked  # Adjust based on your actual models

class PharmacistView(ListView):
    queryset = pharmauser.objects.all()[:10]  # Limit to the first 7 pharmacists
    template_name = 'home/pharmacists.html'
    context_object_name = 'pharm'
    paginate_by = 5  # Adjust pagination as needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Error handling for pharmacistcount
        try:
            context['pharmacistcount'] = PharmacistClicked.objects.with_counts()[:10]
        except AttributeError:
            context['pharmacistcount'] = pharmauser.objects.all()[:10] 
            # Log the error or handle it as necessary

        # Check if querysets are empty
        if not context['pharmacistcount']:
            context['no_pharmacists'] = True
        else:
            context['no_pharmacists'] = False

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise Http404("No pharmacists found.")
        return queryset



def index(request):
    products = Items.objects.all()
    order = Order.objects.all()
    pharmacistclicked = PharmacistClicked.objects.with_counts()
    
    context = {
        'products': products,
        'order': order,
        'pharmacistclicked': pharmacistclicked,
    }
    return render(request, "home/index.html", context)


def pharma_chat(request, pk):
    if request.method == 'POST':
        pharmausers = pharmauser.objects.get(pk=pk)
        user = request.user
        return render(request, 'pharm_chat/chat.html', {'pharmausers': pharmausers})
    return render(request, 'pharm_chat/chat.html')


def signupview(request):
    if request.method == 'POST':
        cleandata = custom_validation(request, request.POST)
        try:
            user = usermodel.objects.create_user(
                email=cleandata['email'], password=cleandata['password']
            )
            user.username = cleandata['username']
            user.save()
            login(request, user)
            return redirect('home:index')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
    
    return render(request, 'home/signup.html')




def signinview(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()  # Strip whitespace
        password = request.POST.get('password', '').strip()

        # Validate email and password
        if not email:
            messages.error(request, 'An email is needed')
        elif not usermodel.objects.filter(email=email).exists():
            messages.error(request, 'User not found with this email')

        if not password:
            messages.error(request, 'A password is needed')
        elif len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')

        # If there are no error messages, authenticate the user
        if not messages.get_messages(request):
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print(user)
                return redirect('home:index')
            else:
                messages.error(request, 'Invalid credentials')

    return render(request, 'home/signin.html')

def pharmsignupview(request):
    if request.method == 'POST':
        data = request.POST
        validated_data = validate_pharmacist(request, data)  # Ensure this function validates the input

        if validated_data:  # Check if validation is successful
            try:
                user = usermodel.objects.create_user(
                    email=validated_data['email'],
                    password=validated_data['password']
                )
                user.save()

                pharm = pharmauser.objects.create(
                    pharmacist=user,
                    name=validated_data['name'],
                    title=validated_data['title'],
                    experience=validated_data['experience'],
                    specialization=validated_data['specialization']
                )
                pharm.save()
                form = ImageForm()
                return render(request, "home/upload.html", {"form": form, "pharm": pharm} )

            except Exception as e:
                messages.error(request, f"Error creating pharmacist account: {str(e)}")
        else:
            messages.error(request, "Invalid input data. Please check your entries.")

    return render(request, 'home/pharmsignup.html')


def uploadimage(request, pk):
    image_location = pharmauser.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form_image = form.cleaned_data['pharm_image']
            image_location.pharm_image = form_image
            image_location.save()
            return redirect('home:login')






def logoutview(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home:index')

    # If the request method is not POST, you might want to return a 405 Method Not Allowed response
    return redirect('home:index')
