from rest_framework import serializers

from ..models import Title


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'russian_name', 'english_name', 'alternative_names', 'description', 'tags', 'volumes']
