# Music App - Models Customized Admin Panel
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from utils.base_utils import get_model

Artist = get_model("music", "Artist")
Album = get_model("music", "Album")
Track = get_model("music", "Track")
TrackPopularity = get_model("music", "TrackPopularity")
AlbumPopularity = get_model("music", "AlbumPopularity")


@admin.register(AlbumPopularity)
class AlbumPopularityAdmin(admin.ModelAdmin):
    list_display = ("artist", "score")
    search_fields = ("artist__stage_name",)
    list_filter = ("artist",)


@admin.register(TrackPopularity)
class TrackPopularityAdmin(admin.ModelAdmin):
    list_display = ("track", "score")
    search_fields = ("track__title",)
    list_filter = ("track",)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "stage_name",
        "user",
        "followers_count",
        "following_count",
        "albums_count",
        "tracks_count",
    )
    search_fields = ("stage_name", "user__username")
    list_filter = ("user",)
    readonly_fields = (
        "followers_count",
        "following_count",
        "albums_count",
        "tracks_count",
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artist",
        "release_date",
        "cover_art",
        "tracks_count",
        "total_duration",
    )
    search_fields = ("name", "artist__stage_name")
    list_filter = ("artist", "release_date")
    readonly_fields = ("tracks_count", "total_duration")
    fieldsets = (
        (
            _("Album Details"),
            {"fields": ("name", "artist", "release_date", "cover_art")},
        ),
    )
    ordering = ("-release_date",)
    date_hierarchy = "release_date"


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "genre", "duration")
    search_fields = ("title", "album__name", "genre")
    list_filter = ("created", "modified")
    readonly_fields = ("duration",)
    fieldsets = (
        (
            _("Track Details"),
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "album",
                    "file",
                    "genre",
                    "artists",
                    "is_active",
                )
            },
        ),
    )
    ordering = ("-created",)
    date_hierarchy = "created"
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("artists",)
    raw_id_fields = ("album",)
    save_on_top = True
