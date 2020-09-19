from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse , HttpResponse
from .models import Update
from django.views.generic import View
from django.core.serializers import serialize

def update_model_detail_view(request):
	data = {
	       "count" : 1000,
	       "content" : "some new content"
	       	}
	#return JsonResponse(data)
	json_data = json.dumps(data)
	return HttpResponse(json_data , content_type='application/json')     


class JsonCBV(View):
	def get(self , request , *args , **kwargs):
		data = {   "count" : 1000 , "content" : "some new content" }
		return JsonResponse(data)

class JsonResponseMixin(object):
	def render_to_json_response(self , context , **response_kwargs):
		return JsonResponse(self.get_data(context) , **response_kwargs)

	def get_data(self , context):
		return context 	

class JsonCBV2(JsonResponseMixin , View):
	def get(self , request , *args , **kwargs):
		data = {
	       "count" : 1000,
	       "content" : "some new content"
	       	}
		return self.render_to_json_response(data)

class SerializeDetailView(View):
	def get(self , request , *args , **kwargs):
		obj = Update.objects.get(id=1)
		json_data = obj.serialize()
		# data = {
		#    "user"    : obj.user.username,
		#    "content" : obj.content 
		# }
		# json_data = json.dumps(data)
		return HttpResponse(json_data , content_type="application/json")


class SerializeListView(View):
    def get(self , request , *args , **kwargs):
    	qs = Update.objects.all()
    	json_data = Update.objects.all().serialize()
    	# data = serialize("json" , qs)
    	# json_data = data
    	return HttpResponse(json_data, content_type="application/json")

    