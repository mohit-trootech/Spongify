from django.urls import path
from music.views import create_album, create_song, list_album, find_artists
from music.constants import Reverse

app_name = "music"

urlpatterns = [
    path("create-album/", create_album, name=Reverse.CREATE_ALBUM),
    path("albums_list/", list_album, name=Reverse.LIST_ALBUM),
    path("find_artists/", find_artists, name=Reverse.FIND_ARTISTS),
    path("create-song/", create_song, name=Reverse.CREATE_SONG),
]
