from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProtoViewSet, ConnectionViewSet, UserDashboardViewSet

router = DefaultRouter()
router.register(r"protos", ProtoViewSet)
router.register(r"connections", ConnectionViewSet)
router.register(r"dashboards", UserDashboardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
