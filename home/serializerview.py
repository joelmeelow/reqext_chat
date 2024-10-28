from django.shortcuts import render
from .serializers import UserRegisterSerializer, UserLoginSerializer, PharmacistRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
from .utils import generate_access_token
import jwt
from .validations import validate_pharmacist, validate_password, validate_email, validate_username, ValidationError, custom_validation



class UserRegistrationAPIView(APIView):
	serializer_class = UserRegisterSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)

	def get(self, request):
		content = { 'message': 'Hello!' }
		return Response(content)

	def post(self, request):
		data = request.data
		cleandata = custom_validation(data)
		if cleandata:
			serializer = self.serializer_class(cleandata)
			if serializer.is_valid(raise_exception=True):
				user = serializer.create(data)
				if user:
					access_token = generate_access_token(user)
					data = { 'access_token': access_token }
					response = Response(data, status=status.HTTP_201_CREATED)
					response.set_cookie(key='access_token', value=access_token, httponly=True)
					return response
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacistRegistratioAPIView(APIView):
	serializer_class = PharmacistRegistrationSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)

	def get(self, request):
		content = { 'message': 'Hello!' }
		return Response(content)

	def post(self, request):
		data = request.data
		cleandata = validate_pharmacist(data)
		if cleandata:
			serializer = self.serializer_class(cleandata)
			if serializer.is_valid(raise_exception=True):
				#using the create_pharmacist method from the serializers module to create a user model, save it, and use it to create the pharmacist model
				user = serializer.create_pharmacist(data)
				if user:
					#generate access token using the method created in the utils module
					access_token = generate_access_token(user)
					data = { 'access_token': access_token }
					response = Response(data, status=status.HTTP_201_CREATED)
					response.set_cookie(key='access_token', value=access_token, httponly=True)
					return response
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)

	def post(self, request):
		email = request.data.get('email', None)
		user_password = request.data.get('password', None)

		if not user_password:
			raise AuthenticationFailed('A user password is needed.')

		if not email:
			raise AuthenticationFailed('An user email is needed.')

		user_instance = authenticate(username=email, password=user_password)

		if not user_instance:
			raise AuthenticationFailed('User not found.')

		if user_instance.is_active:
			user_access_token = generate_access_token(user_instance)
			response = Response()
			response.set_cookie(key='access_token', value=user_access_token, httponly=True)
			response.data = {
				'access_token': user_access_token
			}
			return response

		return Response({
			'message': 'Something went wrong.'
		})

#using a fuction like this, whenever a user wants to access anything in the server, we can verify if the user has registered and therefore has a token
class UserViewAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user_token = request.COOKIES.get('access_token')

		if not user_token:
			raise AuthenticationFailed('Unauthenticated user.')

		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

		user_model = get_user_model()
		user = user_model.objects.filter(user_id=payload['user_id']).first()
		user_serializer = UserRegisterSerializer(user)
		return Response(user_serializer.data)



class UserLogoutViewAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user_token = request.COOKIES.get('access_token', None)
		if user_token:
			response = Response()
			response.delete_cookie('access_token')
			response.data = {
				'message': 'Logged out successfully.'
			}
			return response
		response = Response()
		response.data = {
			'message': 'User is already logged out.'
		}
		return response


