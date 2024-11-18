from django.views.generic import TemplateView
from spongify.constants import Templates


class HomeView(TemplateView):
    template_name = Templates.INDEX


home_view = HomeView.as_view()
