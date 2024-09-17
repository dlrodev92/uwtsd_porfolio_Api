from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet

router = DefaultRouter()
router.register(r'project', TestViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]