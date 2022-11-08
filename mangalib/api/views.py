from django.http import Http404
from rest_framework import views, status, mixins, generics
from rest_framework.response import Response

from remanga.api.models import Title
from remanga.api.serializers import TitleSerializer


class TitleList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TitleDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
