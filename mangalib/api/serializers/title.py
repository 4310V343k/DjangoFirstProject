from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Title


class TitleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = ['url', 'russian_name', 'english_name', 'alternative_names', 'description', 'tags', 'volumes']
