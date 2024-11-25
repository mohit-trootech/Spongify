from django import forms
from utils.base_utils import get_model

Playlist = get_model("library", "Playlist")


class UserPlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["name"]
