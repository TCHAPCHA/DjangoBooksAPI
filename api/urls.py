from tastypie.api import Api
from django.urls import path, include
from .models import BookResource

api = Api(api_name='v1')
api.register(BookResource())

urlpatterns = [
    path('', include(api.urls)),
]