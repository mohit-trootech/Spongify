# Library App Constants


class VerboseNames:
    """Library models - Verbose names"""

    # UserLibrary Model
    USERLIBRARY_O2O_USER = "library"
    USERLIBRARY_M2M_SAVED_TRACKS = "user_saved_tracks"
    USERLIBRARY_M2M_SAVED_ALBUMS = "user_saved_albums"
    USERLIBRARY_M2M_FOLLOWED_ARTISTS = "followers"
    USERLIBRARY_STR = "{user}'s Library"
    LIBRARY = "library"
    LIBRARIES = "libraries"

    # Playlist Model
    PLAYLIST_STR = "{user}'s Playlist"
    PLAYLIST_FK_USER = "playlists"
    PLAYLIST_M2M_TRACKS = "playlists"
    PLAYLIST = "playlist"
    PLAYLISTS = "playlists"


class RequestTypes:
    """Request Types"""

    ADD_SONG = "add_song"
    REMOVE_SONG = "remove_song"
    ADD_ALBUM = "add_album"
    REMOVE_ALBUM = "remove_album"
    FOLLOW_ARTIST = "follow_artist"
    UNFOLLOW_ARTIST = "unfollow_artist"


class AuthMessages:
    """Library App Api Responses Auth Messages"""

    SONG_ADDED = "Song Added Successfully"
    SONG_REMOVED = "Song Removed Successfully"
    ALBUM_ADDED = "Album Added Successfully"
    ALBUM_REMOVED = "Album Removed Successfully"
    ARTIST_FOLLOWED = "Artist Followed Successfully"
    ARTIST_UNFOLLOWED = "Artist Unfollowed Successfully"
