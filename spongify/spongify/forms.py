from django import forms
from utils.constants import FormsClasses


class ArtistLoginForm(forms.Form):
    """Artist Login Form"""

    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": FormsClasses.INPUT}),
        help_text="Verify your username, Check whether you're Artist or Not?",
    )
