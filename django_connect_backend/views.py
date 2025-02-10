import os
import re

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .forms import ConnectionForm
from .models import Connection, UserDashboard, Proto


@login_required
def dashboard(request):
    user_dashboard, created = UserDashboard.objects.get_or_create(user=request.user)
    recent_connections = user_dashboard.recent_connections.order_by("-last_used")[:5]
    all_connections = Connection.objects.filter(user=request.user).order_by("hostname")

    context = {
        "recent_connections": recent_connections,
        "all_connections": all_connections,
    }
    return render(request, "dashboard.html", context)


@login_required
def add_connection(request):
    if request.method == "POST":
        form = ConnectionForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Verbindung erfolgreich hinzugefügt.")
            return redirect("dashboard")
    else:
        form = ConnectionForm(user=request.user)
    return render(request, "add_connection.html", {"form": form})


@login_required
def edit_connection(request, connection_id):
    connection = get_object_or_404(Connection, pk=connection_id, user=request.user)
    if request.method == "POST":
        form = ConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            form.save()
            messages.success(request, "Connection updated successfully.")
            return redirect("dashboard")
    else:
        form = ConnectionForm(instance=connection)
    return render(
        request, "edit_connection.html", {"form": form, "connection": connection}
    )


@login_required
def delete_connection(request, connection_id):
    connection = get_object_or_404(Connection, pk=connection_id, user=request.user)
    if request.method == "POST":
        connection.delete()
        messages.success(request, f'Connection "{connection}" has been deleted.')
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"status": "ok"})
        return redirect("dashboard")
    return render(request, "delete_connection.html", {"connection": connection})


@login_required
def import_putty_connections(request):
    if request.method == "POST" and request.FILES.get("putty_file"):
        putty_file = request.FILES["putty_file"].read().decode("utf-16-le")
        sessions = re.findall(
            r"\[HKEY_CURRENT_USER\\Software\\SimonTatham\\PuTTY\\Sessions\\([^\]]+)\]([^\[]+)",
            putty_file,
        )

        imported_count = 0
        for session_name, session_data in sessions:
            hostname = re.search(r'"HostName"="([^"]+)"', session_data)
            port = re.search(r'"PortNumber"=dword:([0-9a-fA-F]+)', session_data)
            protocol = re.search(r'"Protocol"="([^"]+)"', session_data)

            if hostname and port and protocol:
                hostname = hostname.group(1)
                port = int(port.group(1), 16)
                protocol = protocol.group(1)

                proto, _ = Proto.objects.get_or_create(
                    name=protocol.upper(),
                    defaults={"pref": protocol.lower(), "url_scheme": protocol.lower()},
                )
                Connection.objects.get_or_create(
                    hostname=hostname,
                    port=port,
                    proto=proto,
                    user=request.user,
                    defaults={"name": session_name},
                )
                imported_count += 1

        messages.success(
            request, f"Successfully imported {imported_count} connections."
        )
        return redirect("dashboard")

    return render(request, "import_putty.html")


def download_ps_script(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        "django_connect_backend",
        "static",
        "export_putty_sessions.ps1",
    )
    return FileResponse(
        open(file_path, "rb"), as_attachment=True, filename="export_putty_sessions.ps1"
    )
