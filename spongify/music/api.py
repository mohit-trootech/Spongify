# Music Api Responses
from django.views import View
from django.db.models import Q
from utils.base_utils import get_model
from django.http import JsonResponse
from ast import literal_eval

Album = get_model("music", "Album")
Artist = get_model("music", "Artist")
Track = get_model("music", "Track")


class AlbumsResponses(View):
    def get(self, request, *args, **kwargs):
        """Get album list with filter based on query params"""
        query = Q()
        page = 1
        if request.GET.get("q"):
            query = query | Q(name__icontains=request.GET.get("q"))
        if request.GET.get("artist"):
            query = query | Q(artist__stage_name__icontains=request.GET.get("artist"))
        if request.GET.get("page"):
            page = literal_eval(request.GET.get("page"))
        albums = Album.objects.filter(query).order_by("tracks")[
            (page - 1) * 20 : page * 20
        ]
        data = [
            {
                "id": album.id,
                "name": album.name,
                "artist": album.artist.stage_name,
                "release_date": album.release_date,
                "cover_art": album.cover_art.url if album.cover_art else None,
                "tracks_count": album.tracks_count,
                "duration": album.total_duration,
            }
            for album in albums
        ]
        return JsonResponse(
            data={"data": data},
            safe=False,
        )


album_response = AlbumsResponses.as_view()


class ArtistResponse(View):
    def get(self, request, *args, **kwargs):
        """Get album list with filter based on query params"""
        query = Q()
        page = 1
        if request.GET.get("q"):
            query = query | Q(stage_name__icontains=request.GET.get("q"))
        if request.GET.get("page"):
            page = literal_eval(request.GET.get("page"))
        artists = (
            Artist.objects.filter(query)
            .order_by("followers")
            .order_by("tracks")
            .order_by("albums")[(page - 1) * 20 : page * 20]
        )
        data = [
            {
                "id": artist.id,
                "image": (artist.user.image.url if artist.user.image else None),
                "name": artist.stage_name,
                "albums": artist.albums_count,
                "tracks": artist.tracks_count,
                "popularity": artist.followers_count,
            }
            for artist in artists
        ]
        return JsonResponse(
            data={
                "data": data,
                "total_count": artists.count(),
                "next": f"{request.build_absolute_uri()}?page={page+1}",
                "previous": f"{request.build_absolute_uri()}?page={page-1} if page > 1 else None",
            },
            safe=False,
        )


artist_response = ArtistResponse.as_view()


class TrackResponse(View):
    def get(self, request, *args, **kwargs):
        """Get album list with filter based on query params"""
        query = Q()
        page = 1
        if request.GET.get("q"):
            query = query | Q(title__icontains=request.GET.get("q"))
        if request.GET.get("album"):
            query = query | Q(album__name__icontains=request.GET.get("album"))
        if request.GET.get("artist"):
            query = query | Q(artists__stage_name__icontains=request.GET.get("artist"))
        if request.GET.get("genre"):
            query = query | Q(genre__icontains=request.GET.get("genre"))
        if request.GET.get("page"):
            page = literal_eval(request.GET.get("page"))
        tracks = Track.objects.filter(query).order_by("created")[
            (page - 1) * 20 : page * 20
        ]
        data = [
            {
                "id": track.id,
                "title": track.title,
                "album": track.album.name,
                "genre": track.genre,
                "file": track.file.url,
                "duration": track.duration,
                "artists": [
                    {"id": artist.id, "name": artist.stage_name}
                    for artist in track.artists.all()
                ],
            }
            for track in tracks
        ]
        return JsonResponse(
            data={
                "data": data,
                "total_count": tracks.count(),
                "next": f"{request.build_absolute_uri()}?page={page+1}",
                "previous": f"{request.build_absolute_uri()}?page={page-1} if page > 1 else None",
            },
            safe=False,
        )


track_response = TrackResponse.as_view()


class ArtistTracksResponse(View):
    def get(self, request, *args, **kwargs):
        artist_id = kwargs.get("id")
        if not artist_id:
            return JsonResponse({"error": "artist_id is required"}, status=400)
        try:
            artist = Artist.objects.get(pk=artist_id)
        except Artist.DoesNotExist:
            return JsonResponse({"error": "Artist not found"}, status=404)
        tracks = Track.objects.filter(artists=artist)
        data = [
            {
                "id": track.id,
                "title": track.title,
                "album": track.album.name,
                "genre": track.genre,
                "file": track.file.url,
                "duration": track.duration,
            }
            for track in tracks
        ]
        return JsonResponse({"data": data}, safe=False)


artist_tracks_response = ArtistTracksResponse.as_view()


class AlbumTracksResponse(View):
    def get(self, request, *args, **kwargs):
        album_id = kwargs.get("id")
        if not album_id:
            return JsonResponse({"error": "album_id is required"}, status=400)
        try:
            album = Album.objects.get(pk=album_id)
        except Album.DoesNotExist:
            return JsonResponse({"error": "Album not found"}, status=404)
        tracks = Track.objects.filter(album=album)
        data = [
            {
                "id": track.id,
                "title": track.title,
                "genre": track.genre,
                "file": track.file.url,
                "duration": track.duration,
                "artists": [
                    {"id": artist.id, "name": artist.stage_name}
                    for artist in track.artists.all()
                ],
            }
            for track in tracks
        ]
        return JsonResponse({"data": data}, safe=False)


album_tracks_response = AlbumTracksResponse.as_view()


class TrackApiResponse(View):
    def get(self, request, *args, **kwargs):
        track_id = kwargs.get("id")
        if not track_id:
            return JsonResponse({"error": "track_id is required"}, status=400)
        try:
            track = Track.objects.get(pk=track_id)
        except Track.DoesNotExist:
            return JsonResponse({"error": "Track not found"}, status=404)
        data = {
            "id": track.id,
            "title": track.title,
            "album": track.album.name,
            "genre": track.genre,
            "file": track.file.url,
            "duration": track.duration,
            "artists": [
                {"id": artist.id, "name": artist.stage_name}
                for artist in track.artists.all()
            ],
        }
        return JsonResponse(data, safe=False)


track_api_response = TrackApiResponse.as_view()
