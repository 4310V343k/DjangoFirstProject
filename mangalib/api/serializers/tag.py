from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Tag


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']
