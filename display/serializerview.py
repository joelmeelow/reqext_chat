
from django.shortcuts import render

from display.models import Order
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
from home.utils import generate_access_token
import jwt
from home.validations import validate_pharmacist, validate_password, validate_email, validate_username, ValidationError, custom_validation

from .serializers import ItemSerializer, OrderSerializer
from home.models import Items






#using a fuction like this, whenever a user wants to access anything in the server, we can verify if the user has registered and therefore has a token
class ProductAPIView(APIView):
	serializer_class = ItemSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = [IsAuthenticated]

	def get(self, request):
		#check if the access token was generated for the user
		user_token = request.COOKIES.get('access_token')

		if not user_token:
			raise AuthenticationFailed('Unauthenticated user.')
        #decode the encoded token in the home.utils file
		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        #using the user model to filter the user to see if the decoding was done accordingly
		user_model = get_user_model()
		user = user_model.objects.filter(user_id=payload['user_id']).first()
		#if the user gotten is in the user model, continue to generate the data for the client
		if user.exists():
			items = Items.objects.all()
			#serialize the objects to pytho native types
			serializer = self.serializer_class(items, many=True)
			if serializer.is_valid(raise_exception=True):
				data = serializer.data
				return Response(data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		#logging in again will generate the token again using the client's username
		raise AuthenticationFailed('an error occured, try logging again')
	

class OrderAPIView(APIView):
	serializer_class = OrderSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = [IsAuthenticated]

	def get(self, request):
		#check if the access token was generated for the user
		user_token = request.COOKIES.get('access_token')

		if not user_token:
			raise AuthenticationFailed('Unauthenticated user.')
        #decode the encoded token in the home.utils file
		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        #using the user model to filter the user to see if the decoding was done accordingly
		user_model = get_user_model()
		user = user_model.objects.filter(user_id=payload['user_id']).first()
		#if the user gotten is in the user model, continue to generate the data for the client
		if user.exists():
			order = Order.objects.all()
			#serialize the objects to pytho native types
			serializer = self.serializer_class(order, many=True)
			if serializer.is_valid(raise_exception=True):
				data = serializer.data
				return Response(data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		#logging in again will generate the token again using the client's username
		raise AuthenticationFailed('an error occured, try logging again')
	

	