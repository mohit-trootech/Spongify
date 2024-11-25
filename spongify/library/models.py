from django.db import models
from library.constants import VerboseNames


class UserLibrary(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name=VerboseNames.USERLIBRARY_O2O_USER,
    )
    saved_tracks = models.ManyToManyField(
        "music.Track",
        blank=True,
        related_name=VerboseNames.USERLIBRARY_M2M_SAVED_TRACKS,
    )
    saved_albums = models.ManyToManyField(
        "music.Album",
        blank=True,
        related_name=VerboseNames.USERLIBRARY_M2M_SAVED_ALBUMS,
    )
    followed_artists = models.ManyToManyField(
        "music.Artist",
        blank=True,
        related_name=VerboseNames.USERLIBRARY_M2M_FOLLOWED_ARTISTS,
    )

    def __str__(self):
        return VerboseNames.USERLIBRARY_STR.format(user=self.user.username)

    class Meta:
        verbose_name = VerboseNames.LIBRARY
        verbose_name_plural = VerboseNames.LIBRARIES


class Playlist(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name=VerboseNames.PLAYLIST_FK_USER,
    )
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(
        "music.Track", blank=True, related_name=VerboseNames.PLAYLIST_M2M_TRACKS
    )

    def __str__(self):
        return VerboseNames.PLAYLIST_STR.format(user=self.user.username)

    class Meta:
        verbose_name = VerboseNames.PLAYLIST
        verbose_name_plural = VerboseNames.PLAYLISTS
