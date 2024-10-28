from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from home.models import pharmauser

UserModel = get_user_model()



class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	password2 = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj



		
	


class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	##
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user
	
class PharmacistRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.CharField()
    password1 = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
    password2 = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = pharmauser
        fields = '_all_'

			
    def create_pharmacist(self, clean_data):
        user = UserModel.objects.create_user(
				email=clean_data['email'], password=clean_data['password']
			)
        user.save()
        pharm = pharmauser.objects.create(
			pharmacist = user,
				name = clean_data['name'],
            title = clean_data['title'],
            experince = clean_data['experince'],
            specialization = clean_data['specialization'])
        pharm.save()
        return pharm



