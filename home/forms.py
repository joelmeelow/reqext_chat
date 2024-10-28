from django import forms
from home.models import User, pharmauser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
from django.forms import ModelForm
usermodel = get_user_model()


class SignupForm(forms.ModelForm):
    
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'username']

    widget = {
        'email': forms.EmailInput(attrs={
            'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2 bg-blue-300" #the classname should be the name of the class I will style in my css
           , #this should contain any additional css style
            'placeholder': "enter email",#this should contain what I wantmy placeholder to be
             'id':"email",
             'style': "{'width': 100%, 'margin-top': '10px', 'margin-buttom': '10px', 'padding-left': '5px'}"
        }),
        'username': forms.TextInput(attrs={
            'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2",
           
            "placeholder": "enter username",
            'id':"username"
        }),
        'password': forms.PasswordInput(attrs={
            'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2",
           
            'placeholder': "password",
            'id':"passwordnew2"
        }),
        
    }
    def create(self, clean_data):
        user = usermodel.objects.create_user(
            email=clean_data['email'], password=clean_data['password']
        )
        user.username = clean_data['username']
        user.save()
        return user


class PharmSignupForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = pharmauser
        fields = ['pharmacist', 'name', 'title', 'experience', 'specialization']
 

     #using widget to style the fields
    widget = {
            'email': forms.EmailInput(attrs={
                'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2", #the classname should be the name of the class I will style in my css
              
                'placeholder': "enter email",
                #this should contain what I wantmy placeholder to be
                'id':"username"

            }),
            'username': forms.TextInput(attrs={
                'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2",
              
                "placeholder": "enter username",
                'id':"username"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2",
              
                'placeholder': "password",
                'id':"passwordnew2"
            })
        }


# using mysuermanage modelmanager defined in home.model to create user, and the attach that user to the pharmauser model as a foreignkey
#also create the whole pharmauser object from the sumbmitted form
    def get_pharmacist(self, clean_data):
        user = usermodel.objects.create_user(
            email=clean_data['email'], password=clean_data['password']
        )
        user.save()
        pharm = pharmauser.objects.create(
            pharmacist = user,
            name = clean_data['name'],
            title = clean_data['title'],
            experince = clean_data['experince'],
            specialization = clean_data['specialization']

        )
        pharm.save()
        return pharm
    
   
class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    
    widget = {
        'email': forms.EmailInput(attrs={
            'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2" #the classname should be the name of the class I will style in my css
           , #this should contain any additional css style
            'placeholder': "enter email",#this should contain what I wantmy placeholder to be
            'id':"email"

        }),
     
        'password': forms.PasswordInput(attrs={
            'class': "w-full my-[10px] py-4 px-6 rounded-xl border-2",
           
            'placeholder': "password",
            'id':"passwordnew2"
        })
    }

    def check_signin(self, clean_data):
        user = authenticate(clean_data['email'], clean_data['password'])
        if not user:
            raise forms.ValidationError("user not found")
        return user


class ImageForm(ModelForm):
    class Meta:
        model = pharmauser
        fields = ('pharm_image',)