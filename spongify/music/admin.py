# Music App - Models Customized Admin Panel
from django.contrib import admin
from music.models import Artist, Album, Track
from django.utils.translation import gettext_lazy as _


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("stage_name", "user")
    search_fields = ("stage_name", "user__username")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "artist", "release_date")
    search_fields = ("name", "artist__stage_name")
    list_filter = ("release_date", "artist")


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "created", "modified", "status")
    search_fields = ("title", "album__name", "artists__stage_name")
    list_filter = ("status", "album", "genre", "created", "modified")
    filter_horizontal = ("artists",)
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
                )
            },
        ),
        (_("Activation"), {"fields": ("status",)}),
    )
    readonly_fields = ("slug",)
    ordering = ("-created",)
    date_hierarchy = "created"
