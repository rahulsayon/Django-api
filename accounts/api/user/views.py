from django.contrib.auth import   get_user_model
from rest_framework import permissions , generics , pagination
from . serializers import  UserDetailSerializer
from accounts.api.permissions import AnonPermission 

from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
	#permission_classes  = [permissions.IsAuthenticatedReadOnly]
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserDetailSerializer
	lookup_field = 'username'

# class CFEAPIPagination(pagination.PageNumberPagination):
# 	page_size = 5

class UserStatusAPIView(generics.ListAPIView):
	serializer_class = StatusInlineUserSerializer
	#pagination_class = CFEAPIPagination


	def get_queryset(self,*args,**kwargs):
		username = self.kwargs.get("username" , None)
		if username is None:
			return Status.objects.none()
		return Status.objects.filter(user__username=username)


