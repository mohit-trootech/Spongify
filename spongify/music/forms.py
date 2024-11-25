from django import forms
from utils.base_utils import get_model
from music.constants import HelpTexts, Labels, PlaceHolders
from utils.constants import FormsClasses

Artist = get_model("music", "Artist")
Album = get_model("music", "Album")
Track = get_model("music", "Track")


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("name", "release_date", "cover_art")
        widgets = {}
        labels = {}
        help_texts = {}
        for field in fields:
            input = forms.TextInput
            input_type = "text"
            input_class = FormsClasses.INPUT
            if field == "cover_art":
                input = forms.FileInput
                input_type = "file"
                input_class = FormsClasses.IMAGE_INPUT
            elif field == "release_date":
                input = forms.DateTimeInput
                input_type = "datetime-local"
                input_class = FormsClasses.INPUT
            widgets[field] = input(
                attrs={
                    "class": input_class,
                    "placeholder": PlaceHolders.ALBUM[field],
                    "type": input_type,
                }
            )
            labels[field] = Labels.ALBUM[field]


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ("title", "file", "genre")
        widgets = {}
        labels = {}
        help_texts = {}
        for field in fields:
            input_type = forms.TextInput
            input_class = FormsClasses.INPUT
            if field == "file":
                input_type = forms.FileInput
                input_class = FormsClasses.IMAGE_INPUT
            elif field == "genre":
                input_type = forms.Select
                input_class = FormsClasses.SELECT
            widgets[field] = input_type(
                attrs={"class": input_class, "placeholder": PlaceHolders.TRACK[field]}
            )
            labels[field] = Labels.TRACK[field]
            help_texts[field] = HelpTexts.TRACK[field]
