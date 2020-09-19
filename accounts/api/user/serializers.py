from django.contrib.auth import get_user_model
from rest_framework import serializers
import datetime
from django.utils import timezone

from status.api.serializers import StatusInlineUserSerializer


User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
	uri           = serializers.SerializerMethodField(read_only=True)
	status        = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = User
		fields = [
 				'id',
 				'username',
 				'uri',
 				'status',
		]
	
	def get_uri(self, obj):
		return "/api/users/{id}/".format(id=obj.id)

	def get_status(self,obj):
		request = self.context.get('request') 
		qs = obj.status_set.all().order_by("-timestamp")[:10]
		data  = {
           'uri': self.get_uri(obj) + "status/",
           'last' : StatusInlineUserSerializer(qs.first()).data ,
           'recent' : StatusInlineUserSerializer(qs[:10],many=True).data
		}
		return data

	# def get_recent_status(self,obj):
	# 	qs = obj.status_set.all().order_by("-timestamp")[:10]
	# 	return StatusInlineUserSerializer(qs,many=True).data