from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Chapter


class ChapterSerializer(HyperlinkedModelSerializer):
    volume_url = serializers.HyperlinkedRelatedField(view_name='volume-details', read_only=True)

    class Meta:
        model = Chapter
        fields = ['url', 'volume_url', 'name', 'position', 'watch_count', 'like_count']
