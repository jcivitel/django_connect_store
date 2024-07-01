from django.db import models


class Proto(models.Model):
    pid = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20)
    pref = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Connection(models.Model):
    connid = models.IntegerField(primary_key=True, auto_created=True)
    hostname = models.CharField(max_length=200)
    port = models.IntegerField(max_length=20000)
    proto = models.ForeignKey('Proto', models.DO_NOTHING)

    def __str__(self):
        return f"{self.hostname} using {self.proto.name}"
