# Library App Constants


class VerboseNames:
    """Library models - Verbose names"""

    # UserLibrary Model
    USERLIBRARY_O2O_USER = "library"
    USERLIBRARY_M2M_SAVED_TRACKS = "saved_by"
    USERLIBRARY_M2M_SAVED_ALBUMS = "saved_by"
    USERLIBRARY_M2M_FOLLOWED_ARTISTS = "followers"
    USERLIBRARY_STR = "{user}'s Library"
    LIBRARY = "library"
    LIBRARIES = "libraries"

    # Playlist Model
    PLAYLIST_STR = "{user}'s Playlist"
    PLAYLIST_FK_USER = "user"
    PLAYLIST_M2M_TRACKS = "playlists"
    PLAYLIST = "playlist"
    PLAYLISTS = "playlists"
