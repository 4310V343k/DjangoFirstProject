from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Volume


class VolumeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Volume
        fields = ['url', 'title', 'name', 'cost', 'position', 'chapters']
