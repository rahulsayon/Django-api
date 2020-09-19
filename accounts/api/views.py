from django.contrib.auth import authenticate , get_user_model
from django.db.models import Q
from rest_framework import permissions , generics
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

from rest_framework_jwt.settings import api_settings
from . serializers import UserRegisterSerializer , UserDetailSerializer
from . permissions import AnonPermission

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserDetailSerializer
	lookup_field = 'username'


class AuthView(APIView):
	permission_classes = [permissions.AllowAny]
	def post(self , request , *args , **kwargs):
		print(request.user)
		if request.user.is_authenticated:
			return Response({'detail' : 'You are already authenticated'} , status=400)
		data = request.data
		username = data.get('username')
		password = data.get('password')
		print(username)
		user = authenticate(username=username , password=password)
		qs = User.objects.filter(
              Q(username__iexact=username)| 
              Q(email__iexact=username) 
			).distinct()
		if qs.count() == 1:
			user_obj = qs.first()
			if user_obj.check_password(password):
				user = user_obj
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				response = jwt_response_payload_handler(token , user , request=request)
				return Response(response)

		return Response({"details" : "Invalid credentials"} , status=401)


class RegisterView(APIView):
	permission_classes = [permissions.AllowAny]
	def post(self , request , *args , **kwargs):
		#print(request.user)
		if request.user.is_authenticated:
			return Response({'detail' : 'You are already authenticated'} , status=400)
		data = request.data
		username = data.get('username')
		email = data.get('username')
		password = data.get('password')
		password2 = data.get('password2')
		print(username)
		
		qs = User.objects.filter(
              Q(username__iexact=username)| 
              Q(email__iexact=username) 
			).distinct()
		if password != password2:
			return Response({'password' : 'password must watch'} , status=401)
		if qs.exists():
			return Response({'details' : "This user already exits"} , status=401)
		else:
			user = User.objects.create(username=username , email=email)
			user.set_password(password)
			user.save()
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
			response = jwt_response_payload_handler(token , user , request=request)
			return Response(response)
		
		return Response({"details" : "Invalid Request"} , status=400)


class RegisterAPIView(generics.CreateAPIView):
	queryset           =  User.objects.all()
	serializer_class   =  UserRegisterSerializer
	permission_classes =  [AnonPermission]
	#permission_classes =  [permissions.AllowAny]

	def get_serializer_context(self,*args,**kwargs):
		return {"request" : self.request}