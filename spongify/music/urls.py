from django.urls import path
from music.views import creator_view, creator_join
from music.constants import Reverse

app_name = "music"

urlpatterns = [
    path("creator/", creator_view, name=Reverse.CREATOR),
    path("creator/join/", creator_join, name=Reverse.CREATOR_JOIN),
]
