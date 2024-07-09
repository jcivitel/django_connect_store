from rest_framework import viewsets
from django_connect_backend.models import Proto, Connection, UserDashboard
from .serializers import ProtoSerializer, ConnectionSerializer, UserDashboardSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ProtoViewSet(viewsets.ModelViewSet):
    queryset = Proto.objects.all()
    serializer_class = ProtoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UserDashboardViewSet(viewsets.ModelViewSet):
    queryset = UserDashboard.objects.all()
    serializer_class = UserDashboardSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
