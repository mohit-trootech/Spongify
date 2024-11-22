from django.urls import path
from library.views import user_album

app_name = "library"

urlpatterns = [
    path("user-album/", user_album, name="user-album"),
]
