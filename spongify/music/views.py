from django.views.generic import TemplateView
from music.constants import Templates


class CreateAlbumView(TemplateView):
    template_name = Templates.CREATE_ALBUM


create_album = CreateAlbumView.as_view()
