from django.db import models
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .authentication import UserAuthentication

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        allowed_methods = ['get', 'post', 'delete']
        authentication = UserAuthentication()
        authorization = Authorization()
        filtering = {
            'title': ('exact', 'contains'),
            'author': ('exact', 'contains'),
            'genre': ('exact', 'contains'),
            'status': ('exact', 'contains'),
        }