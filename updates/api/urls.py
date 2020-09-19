from django.conf.urls import url
from .views import (
        
          UpdateModelListAPIView,
          UpdateModelDetailAPIView
	)


urlpatterns = [

    url(r'^$', UpdateModelListAPIView.as_view() ),
    url(r'^(?P<id>\d+)$', UpdateModelDetailAPIView.as_view() ),
]
