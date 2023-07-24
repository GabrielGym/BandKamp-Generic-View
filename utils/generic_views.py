from rest_framework.views import APIView
from .mixin import (
    CreateSongModelMixin,
)


class GenericAPIView(APIView):
    queryset = None
    queryset_album = None
    serializer_class = None
    lookup_field = "pk"


class CreateSongAPIView(GenericAPIView, CreateSongModelMixin):
    def post(self, request, *args: tuple, **kwargs: dict):
        return super().create(request, *args, **kwargs)