from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('titles', views.TitleViewSet, basename='title')
router.register('volumes', views.VolumeViewSet, basename='volume')
router.register('chapters', views.ChapterViewSet, basename='chapter')
router.register('tags', views.TagViewSet, basename='tag')


urlpatterns = [
    path('', include(router.urls)),
]
