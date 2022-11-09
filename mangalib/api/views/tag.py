from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mangalib.api.models import Tag
from mangalib.api.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
