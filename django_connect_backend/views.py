from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ConnectionForm
from .models import Connection, UserDashboard


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
            connection = form.save()
            messages.success(request, "Verbindung erfolgreich hinzugefügt.")
            return redirect("dashboard")
    else:
        form = ConnectionForm(user=request.user)
    return render(request, "add_connection.html", {"form": form})
