#from django.shortcuts import render

# Create your views here.
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from updates.mixin import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin
import json


class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):

	is_json = True

	def get(self , request , id ,*args , **kwargs):
		obj = UpdateModel.objects.get(id=1)
		json_data = obj.serialize()
		return 	self.render_to_response(json_data)


	def post(self , request , *args , **kwargs):
	    json_data = {}
	    return 	self.render_to_response(json_data)


	def put(self , request , *args, **kwargs):
		json_data = {}
		return 	self.render_to_response(json_data)


	def delete(self , request , *args , **kwargs):
		json_data = {}
		return	self.render_to_response(json_data , status=403)
		


class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
	
    is_json = True

    def get(self , request , *args , **kwargs):
    	qs = UpdateModel.objects.all()
    	json_data = qs.serialize()
    	#return HttpResponse(json_data , content_type='application/json')
    	return self.render_to_response(data)

    def post(self , request , *args , **kwargs):
    	data = json.dumps({"message" : "Unkonw data"})
    	#return HttpResponse(data , content_type='application/json')
    	return self.render_to_response(data , status=400)

    def delete(self , request , *args , **kwargs):
    	data = json.dumps({"message" : "you can not delete an entire list"})
    	status_code = 403
    	return self.render_to_response(data, status=403)
    	