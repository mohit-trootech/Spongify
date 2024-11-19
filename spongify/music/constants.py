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
    """Music Template Paths"""

    CREATOR_TEMPLATE = "music/creator.html"


class Reverse:
    """Music Template Urls Reverse"""

    CREATOR = "creator"
    CREATOR_JOIN = "creator-join"


class AuthErrors:
    """Music Authentication Errors"""

    NOT_REGISTERED = "User is not authenticated, Login to continue."


class AuthMessages:
    """Music Authentication Messages"""

    CREATOR_REGISTRATION_JOINED = (
        "You successfully joined the waitlist, Check email for updates."
    )


class UrlPaths:
    """Music Url Paths"""

    CREATOR = "/spongify/creator/"
    CREATOR_JOIN = "/spongify/creator/join/"
