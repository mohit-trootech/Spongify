from django.db.models import (
    ImageField,
    CharField,
    ForeignKey,
    Model,
    OneToOneField,
    CASCADE,
    FileField,
    ManyToManyField,
    DateTimeField,
)
from django_extensions.db.models import (
    TitleSlugDescriptionModel,
    TimeStampedModel,
    ActivatorModel,
)
from music.constants import VerboseNames, Choice


def _album_cover_upload_to(instance, filename):
    return "album_covers/{name}/{filename}".format(
        name=instance.name, filename=filename
    )


def _tracks_upload_to(instance, filename):
    return "tracks/{slug}/{filename}".format(slug=instance.slug, filename=filename)


class Artist(Model):
    stage_name = CharField(
        max_length=100, unique=True, verbose_name=VerboseNames.STAGE_NAME
    )
    user = OneToOneField(
        "accounts.User", on_delete=CASCADE, related_name=VerboseNames.ARTIST_O2O_USER
    )

    def __str__(self):
        return self.stage_name

    class Meta:
        verbose_name = VerboseNames.ARTIST
        verbose_name_plural = VerboseNames.ARTISTS


class Album(Model):
    name = CharField(max_length=100)
    artist = ForeignKey(
        "music.Artist", on_delete=CASCADE, related_name=VerboseNames.ALBUM_FK_ARTIST
    )
    release_date = DateTimeField(verbose_name=VerboseNames.RELEASE_DATE)
    cover_art = ImageField(
        upload_to=_album_cover_upload_to, verbose_name=VerboseNames.COVER_ART
    )

    def __str__(self):
        return VerboseNames.ALBUM_STR.format(
            name=self.name, artist=self.artist.stage_name
        )


class Track(TitleSlugDescriptionModel, ActivatorModel, TimeStampedModel):
    album = ForeignKey(
        "music.Album", on_delete=CASCADE, related_name=VerboseNames.TRACK_FK_ALBUM
    )
    file = FileField(upload_to=_tracks_upload_to)
    genre = CharField(
        choices=Choice.GENRE_CHOICES,
        max_length=100,
        default=Choice.OTHER,
        verbose_name=VerboseNames.GENRE,
    )
    artists = ManyToManyField(
        "music.Artist", related_name=VerboseNames.TRACK_M2M_ARTIST
    )

    def __str__(self):
        return f"{self.album.name} - {self.title}"

    class Meta:
        verbose_name = VerboseNames.TRACK
        verbose_name_plural = VerboseNames.TRACKS
