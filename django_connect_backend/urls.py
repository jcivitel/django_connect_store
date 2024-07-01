from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("connect/<int:connection_id>/", views.connect, name="connect"),
    path('add-connection/', views.add_connection, name='add_connection'),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="dashboard"), name="logout"
    ),
]
