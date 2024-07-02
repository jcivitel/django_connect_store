from django.urls import path

from . import views

urlpatterns = [
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
