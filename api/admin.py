from django.contrib import admin
from api import models

admin.site.site_header = "Books Admin Panel"
admin.site.site_title = "Books"
admin.site.index_title = "Welcome to Books Admin Panel"

admin.site.register(models.Book)
