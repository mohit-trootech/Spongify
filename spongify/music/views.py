from django.views.generic import TemplateView, View
from music.constants import Templates
from django.shortcuts import redirect
from music.tasks import artist_signup_mail_task
from django.contrib.messages import info
from music.constants import AuthErrors, AuthMessages, UrlPaths
from utils.base_utils import get_model

CreatorWaitlist = get_model(app_name="spongify", model_name="CreatorWaitlist")


class CreatorView(TemplateView):
    template_name = Templates.CREATOR_TEMPLATE


creator_view = CreatorView.as_view()


class CreatorJoinView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            info(request=request, message=AuthErrors.NOT_REGISTERED)
        else:
            info(request=request, message=AuthMessages.CREATOR_REGISTRATION_JOINED)
        CreatorWaitlist.objects.create(user=request.user)
        artist_signup_mail_task.delay(self.request.user.id)
        return redirect(UrlPaths.CREATOR)


creator_join = CreatorJoinView.as_view()
