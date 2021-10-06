# Generated by Django 3.2.8 on 2021-10-06 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('connid', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=200)),
                ('programm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='django_connect_backend.programms')),
            ],
        ),
    ]
