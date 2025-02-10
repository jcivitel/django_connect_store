from django.contrib.auth.models import User
from django.db import models


class Proto(models.Model):
    name = models.CharField(max_length=20)
    pref = models.CharField(max_length=20)
    url_scheme = models.CharField(max_length=20, default="ssh")  # Neues Feld

    def __str__(self):
        return self.name


class Connection(models.Model):
    name = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200)
    port = models.IntegerField()
    proto = models.ForeignKey(Proto, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else f"{self.hostname}:{self.port}"

    def get_connection_url(self):
        return f"{self.proto.url_scheme}://{self.hostname}:{self.port}"


class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recent_connections = models.ManyToManyField(Connection)

    def __str__(self):
        return f"Dashboard for {self.user.username}"
