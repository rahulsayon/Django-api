"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from updates.views import update_model_detail_view , JsonCBV , JsonCBV2, SerializeDetailView , SerializeListView
from updates.api.views import UpdateModelDetailAPIView
from status.api.views  import (StatusListSearchAPIView , StatusAPIView , 
    StatusCreateAPIView , StatusDetailAPIView ,
    StatusUpdateAPIView  , StatusDeleteAPIView , StatusAPIDetailView) 
from rest_framework_jwt.views import obtain_jwt_token , refresh_jwt_token
from accounts.api.views import AuthView , RegisterView , RegisterAPIView 
from accounts.api.user.views import   UserDetailAPIView , UserStatusAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/updates/$', include('updates.api.urls')),
    url(r'^api/auth/jwt/$', obtain_jwt_token ),
    url(r'^api/auth/jwt/refresh/$', refresh_jwt_token ),
    url(r'^api/auth/$', AuthView.as_view() ),
    url(r'^api/auth/register/$', RegisterView.as_view() ),
    url(r'^api/auth/apiregister/', RegisterAPIView.as_view() ),
    url(r'^api/status/$', include('status.api.urls')),
    # url(r'^$', update_model_detail_view ),
    url(r'^json/cbv/$', JsonCBV.as_view() ),
    url(r'^json/cbv2/$', JsonCBV2.as_view() ),
    url(r'^json/serialized/details/$', SerializeDetailView.as_view() ),
    url(r'^json/serialized/list/$', SerializeListView.as_view() ),
    url(r'^api/updates/(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view() ),

    #url(r'^api/status/(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    url(r'^api/status/(?P<pk>\d+)/$', StatusAPIDetailView.as_view()),
    url(r'^api/status/(?P<pk>\d+)/update$', StatusUpdateAPIView.as_view()),
    url(r'^api/status/(?P<pk>\d+)/delete$', StatusDeleteAPIView.as_view()),
    url(r'^api/user/(?P<username>\w+)/$', UserDetailAPIView.as_view()  , name="details"),
    url(r'^api/user/(?P<username>\w+)/status$', UserStatusAPIView.as_view()  ),


]
