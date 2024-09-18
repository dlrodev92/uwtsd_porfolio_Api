from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SubtitleViewSet, ParagraphViewSet, ReferenceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'subtitles', SubtitleViewSet)
router.register(r'paragraphs', ParagraphViewSet)
router.register(r'references', ReferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
