from django.db.models.manager import BaseManager
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from mangalib.api.models import Volume, Title
from mangalib.api.serializers import VolumeSerializer


class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
