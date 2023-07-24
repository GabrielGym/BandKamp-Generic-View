from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404


class CreateSongModelMixin:
    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        lookup_field = kwargs.get(self.lookup_field)
        album = get_object_or_404(self.queryset_album, pk=lookup_field)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(album=album)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)