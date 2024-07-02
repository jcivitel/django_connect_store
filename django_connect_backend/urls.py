from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-connection/", views.add_connection, name="add_connection"),
    path('edit-connection/<int:connection_id>/', views.edit_connection, name='edit_connection'),
]
