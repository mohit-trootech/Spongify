# Library App - Models Customized Admin Panel

from django.contrib import admin
from library.models import UserLibrary, Playlist
from django.utils.translation import gettext_lazy as _


@admin.register(UserLibrary)
class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username",)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
    search_fields = ("user__username", "name")
    filter_horizontal = ("tracks",)
    fieldsets = ((_("Playlist Details"), {"fields": ("user", "name", "tracks")}),)
