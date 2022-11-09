from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Volume


class VolumeSerializer(HyperlinkedModelSerializer):
    title_url = serializers.HyperlinkedRelatedField(view_name='title-details', read_only=True)

    class Meta:
        model = Volume
        fields = ['url', 'title_url', 'name', 'cost', 'position', 'chapters']
