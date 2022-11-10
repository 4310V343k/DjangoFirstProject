from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Chapter


class ChapterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ['url', 'volume', 'name', 'position', 'watch_count', 'like_count']
