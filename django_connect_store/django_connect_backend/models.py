from django.db import models


class Programms(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Connection(models.Model):
    connid = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=200)
    port = models.IntegerField
    programm = models.ForeignKey('Programms', models.DO_NOTHING)

    def __str__(self):
        return self.hostname + ' using ' + self.programm.name
