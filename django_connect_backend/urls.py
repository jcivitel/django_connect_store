from django.urls import path
from django.urls import re_path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='dashboard', permanent=True)),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-connection/", views.add_connection, name="add_connection"),
    path(
        "edit-connection/<int:connection_id>/",
        views.edit_connection,
        name="edit_connection",
    ),
    path("import-putty/", views.import_putty_connections, name="import_putty"),
    path("download-ps-script/", views.download_ps_script, name="download_ps_script"),
    path(
        "delete-connection/<int:connection_id>/",
        views.delete_connection,
        name="delete_connection",
    ),
]
