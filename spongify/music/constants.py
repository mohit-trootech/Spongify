# Music app constants
from django.utils.translation import gettext_noop as _


class Choice:
    """Music Model Choices"""

    POP = "pop"
    ROCK = "rock"
    HIP_HOP = "hip_hop"
    ELECTRONIC = "electronic"
    JAZZ = "jazz"
    CLASSICAL = "classical"
    COUNTRY = "country"
    RNB = "r_n_b"
    REGGAE = "reggae"
    FOLK = "folk"
    BLUES = "blues"
    METAL = "metal"
    PUNK = "punk"
    ALTERNATIVE = "alternative"
    INDIE = "indie"
    OTHER = "other"

    GENRE_CHOICES = (
        (POP, _("Pop")),
        (ROCK, _("Rock")),
        (HIP_HOP, _("Hip Hop")),
        (ELECTRONIC, _("Electronic")),
        (JAZZ, _("Jazz")),
        (CLASSICAL, _("Classical")),
        (COUNTRY, _("Country")),
        (RNB, _("R&B")),
        (REGGAE, _("Reggae")),
        (FOLK, _("Folk")),
        (BLUES, _("Blues")),
        (METAL, _("Metal")),
        (PUNK, _("Punk")),
        (ALTERNATIVE, _("Alternative")),
        (INDIE, _("Indie")),
        (OTHER, _("Other")),
    )


class VerboseNames:
    """Music Model Verbose Names"""

    # Artist
    ARTIST = "artist"
    ARTISTS = "artists"
    STAGE_NAME = "Stage Name"
    ARTIST_O2O_USER = "artist"

    # Album
    ALBUM = "album"
    ALBUMS = "albums"
    RELEASE_DATE = "Release Date"
    COVER_ART = "Cover Art"
    ALBUM_FK_ARTIST = "albums"
    ALBUM_STR = "{name} by {artist}"

    # Track
    TRACK = "track"
    TRACKS = "tracks"
    TRACK_FK_ALBUM = "tracks"
    TRACK_M2M_ARTIST = "tracks"
    GENRE = "Genre"


class Templates:
    """Music App Templates"""

    CREATE_ALBUM = "music/create_album.html"
    LIST_ALBUM = "music/list_album.html"
    CREATE_SONG = "music/create_song.html"


class Reverse:
    """Music App Urls Reverse"""

    CREATE_ALBUM = "create-album"
    LIST_ALBUM = "list-album"
    CREATE_SONG = "create-song"
    LIST_SONG = "list-song"
    FIND_ARTISTS = "find-artists"
    API_ALBUM = "album-response"


class HelpTexts:
    """Music App Form Help Texts"""

    ALBUM = {
        "cover_art": "Please choose a high quality cover art, please use your own materials.",
        "release_date": "This date & time will be used to release this album world wide.",
    }
    TRACK = {
        "title": "Enter track title",
        "album": "Select track album",
        "file": "Upload track file",
        "genre": "Select track genre",
        "artists": "Select track artists",
    }


class Labels:
    """Music App Form Labels"""

    ALBUM = {
        "name": "Enter album name",
        "cover_art": "Upload album cover art",
        "release_date": "Select album release date",
    }
    TRACK = {
        "title": "Enter track title",
        "album": "Select track album",
        "file": "Upload track file",
        "genre": "Select track genre",
        "artists": "Select track artists",
    }


class PlaceHolders:
    """Music App Form PlaceHolders"""

    ALBUM = {
        "name": "Enter album name",
        "cover_art": "Upload album cover art",
        "release_date": "Select album release date",
    }
    TRACK = {
        "title": "Enter track title",
        "album": "Select track album",
        "file": "Upload track file",
        "genre": "Select track genre",
        "artists": "Select track artists",
    }
