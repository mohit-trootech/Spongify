from django.urls import path
from music.views import create_album
from music.constants import Reverse

app_name = "music"

urlpatterns = [path("create-album/", create_album, name=Reverse.CREATE_ALBUM)]
