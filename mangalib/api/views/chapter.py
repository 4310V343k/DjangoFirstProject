from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from mangalib.api.models import Chapter
from mangalib.api.serializers import ChapterSerializer
from mangalib.api.tasks import increment_chapter_watch, increment_chapter_like


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def retrieve(self, *args, **kwargs):
        increment_chapter_watch.delay(pk=kwargs['pk'])
        return super(ChapterViewSet, self).retrieve(*args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def like(self, *args, **kwargs):
        increment_chapter_like.delay(pk=kwargs['pk'])
        return super(ChapterViewSet, self).retrieve(*args, **kwargs)

    permission_classes = [IsAuthenticatedOrReadOnly]
