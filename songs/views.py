from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
from utils.generic_views import CreateSongAPIView


class SongView(generics.ListAPIView, CreateSongAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    queryset_album = Album
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)