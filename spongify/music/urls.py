from django.urls import path
from music.views import create_album, create_song, list_album, find_artists
from music.constants import Reverse
from music.api import (
    album_response,
    artist_response,
    track_response,
    artist_tracks_response,
    album_tracks_response,
    track_api_response,
)


app_name = "music"

urlpatterns = [
    path("create-album/", create_album, name=Reverse.CREATE_ALBUM),
    path("albums_list/", list_album, name=Reverse.LIST_ALBUM),
    path("find_artists/", find_artists),
    path("create-song/", create_song, name=Reverse.CREATE_SONG),
    path("album-response/", album_response),
    path("artist-response/", artist_response),
    path("tracks-response/", track_response),
    path("artist-tracks-response/<int:id>", artist_tracks_response),
    path("album-tracks-response/<int:id>", album_tracks_response),
    path("tracks-api-response/<int:id>", track_api_response),
]
