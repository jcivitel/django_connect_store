from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps

for model in apps.get_app_config('django_connect_backend').models.values():
    admin.site.register(model)
