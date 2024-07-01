from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ConnectionForm
from .models import Connection, UserDashboard


@login_required
def dashboard(request):
    user_dashboard, created = UserDashboard.objects.get_or_create(user=request.user)
    recent_connections = user_dashboard.recent_connections.order_by("-last_used")[:5]
    return render(request, "dashboard.html", {"recent_connections": recent_connections})


@login_required
def connect(request, connection_id):
    connection = Connection.objects.get(pk=connection_id)
    # Hier würde die Logik für die SSH-Verbindung implementiert
    # Aktualisieren Sie das Dashboard
    user_dashboard, created = UserDashboard.objects.get_or_create(user=request.user)
    user_dashboard.recent_connections.add(connection)
    return render(request, "connect.html", {"connection": connection})


@login_required
def add_connection(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST, user=request.user)
        if form.is_valid():
            connection = form.save()
            messages.success(request, 'Verbindung erfolgreich hinzugefügt.')
            return redirect('dashboard')
    else:
        form = ConnectionForm(user=request.user)
    return render(request, 'add_connection.html', {'form': form})
