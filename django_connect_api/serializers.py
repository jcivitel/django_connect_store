from rest_framework import serializers
from django_connect_backend.models import Proto, Connection, UserDashboard


class ProtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proto
        fields = "__all__"


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"


class UserDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDashboard
        fields = "__all__"
