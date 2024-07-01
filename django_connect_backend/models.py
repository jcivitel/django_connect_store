from django.db import models
from django.contrib.auth.models import User

class Proto(models.Model):
    pid = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20)
    pref = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Connection(models.Model):
    connid = models.IntegerField(primary_key=True, auto_created=True)
    hostname = models.CharField(max_length=200)
    port = models.IntegerField()
    proto = models.ForeignKey('Proto', models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hostname} using {self.proto.name}"

class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recent_connections = models.ManyToManyField(Connection)

    def __str__(self):
        return f"Dashboard for {self.user.username}"