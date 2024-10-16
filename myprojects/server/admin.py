from django.contrib import admin
from .models import Server, Channel, Category

admin.site.register(Server)
admin.site.register(Category)
admin.site.register(Channel)