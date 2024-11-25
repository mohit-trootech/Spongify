from django.views.generic import FormView, View
from django.contrib.messages.views import SuccessMessageMixin
from music.constants import Templates
from music.forms import AlbumForm, TrackForm
from utils.base_utils import get_model
from django.db.models import Q
from django.http import JsonResponse
from music.constants import AuthErrors

Artist = get_model("music", "Artist")
Album = get_model("music", "Album")


class CreateAlbumView(FormView, SuccessMessageMixin):
    template_name = Templates.CREATE_ALBUM
    form_class = AlbumForm
    success_url = "/"

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, AuthErrors.UNAUTHENTICATED)
            return self.form_invalid(form)
        if not Artist.objects.filter(user=self.request.user).exists():
            form.add_error(None, AuthErrors.NOT_ARTIST)
            return self.form_invalid(form)
        album = form.save(commit=False)
        album.artist = Artist.objects.get(user=self.request.user)
        album.save()
        return super().form_valid(form)


create_album = CreateAlbumView.as_view()


class CreateSongView(FormView):
    template_name = Templates.CREATE_SONG
    form_class = TrackForm
    success_url = "/"

    def form_valid(self, form):
        track = form.save(commit=False)
        artists = self.request.POST.getlist("artists")
        album = self.request.POST.get("album")
        track.album = Album.objects.get(id=album)
        track.artists.set(artists)
        track.save()
        return super().form_valid(form)


create_song = CreateSongView.as_view()


class AlbumList(View):
    def get(self, request, *args, **kwargs):
        """Get album list with filter based on query params"""
        query = Q()
        if request.GET.get("q"):
            query = query | Q(name__icontains=request.GET.get("q"))
        albums = Album.objects.filter(query)[:20]
        data = [{"id": album.id, "name": album.name} for album in albums]
        return JsonResponse({"items": data, "total_count": albums.count()}, safe=False)


list_album = AlbumList.as_view()


class FindArtists(View):
    def get(self, request, *args, **kwargs):
        """Get artist list with filter based on query params"""
        query = Q()
        if request.GET.get("q"):
            query = query | Q(stage_name__icontains=request.GET.get("q"))
        artists = Artist.objects.filter(query)[:20]
        data = [{"id": artist.id, "name": artist.stage_name} for artist in artists]
        return JsonResponse({"items": data, "total_count": artists.count()}, safe=False)


find_artists = FindArtists.as_view()
