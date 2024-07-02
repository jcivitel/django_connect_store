from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-connection/", views.add_connection, name="add_connection"),
]
