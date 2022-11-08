from rest_framework import serializers

from ..models import Volume


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['title', 'name', 'cost', 'position', 'chapters']
