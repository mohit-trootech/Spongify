from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ast import literal_eval
from utils.base_utils import get_model
from django.http import JsonResponse
from library.constants import RequestTypes, AuthMessages


@method_decorator(csrf_exempt, name="dispatch")
class UserAlbum(View):
    def post(self, request, *args, **kwargs):
        """Add Song to Liked Songs"""
        request_data = literal_eval(request.body.decode("utf-8"))
        try:
            if request_data["type"] == RequestTypes.ADD_SONG:
                song_id = request_data["id"]
                model = get_model("music", "Track")
                song = model.objects.get(pk=song_id)
                user_library = request.user.library
                user_library.saved_tracks.add(song)
                return JsonResponse({"message": AuthMessages.SONG_ADDED})
            elif request_data["type"] == RequestTypes.REMOVE_SONG:
                song_id = request_data["id"]
                model = get_model("music", "Track")
                song = model.objects.get(pk=song_id)
                user_library = request.user.library
                user_library.saved_tracks.remove(song)
                return JsonResponse({"message": AuthMessages.SONG_REMOVED})
            elif request_data["type"] == RequestTypes.ADD_ALBUM:
                album_id = request_data["id"]
                model = get_model("music", "Album")
                album = model.objects.get(pk=album_id)
                user_library = request.user.library
                user_library.saved_albums.add(album)
                return JsonResponse({"message": AuthMessages.ALBUM_ADDED})
            elif request_data["type"] == RequestTypes.REMOVE_ALBUM:
                album_id = request_data["id"]
                model = get_model("music", "Album")
                album = model.objects.get(pk=album_id)
                user_library = request.user.library
                user_library.saved_albums.remove(album)
                return JsonResponse({"message": AuthMessages.ALBUM_REMOVED})
            elif request_data["type"] == RequestTypes.FOLLOW_ARTIST:
                artist_id = request_data["id"]
                model = get_model("music", "Artist")
                artist = model.objects.get(pk=artist_id)
                user_library = request.user.library
                user_library.followed_artists.add(artist)
                return JsonResponse({"message": AuthMessages.ARTIST_FOLLOWED})
            elif request_data["type"] == RequestTypes.UNFOLLOW_ARTIST:
                artist_id = request_data["id"]
                model = get_model("music", "Artist")
                artist = model.objects.get(pk=artist_id)
                user_library = request.user.library
                user_library.followed_artists.remove(artist)
                return JsonResponse({"message": AuthMessages.ARTIST_UNFOLLOWED})
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)


user_album = UserAlbum.as_view()
