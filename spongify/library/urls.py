from django.urls import path
from library.views import user_album, playlist_view

app_name = "library"

urlpatterns = [
    path("user-album/", user_album, name="user-album"),
    path("playlist-view/", playlist_view, name="playlist-view"),
]
