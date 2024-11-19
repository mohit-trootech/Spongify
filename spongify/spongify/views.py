from django.views.generic import TemplateView, FormView, View
from spongify.constants import AuthErrors, AuthMessages, UrlPaths, Templates
from utils.base_utils import get_model
from django.shortcuts import redirect
from spongify.tasks import artist_signup_mail_task
from django.contrib.messages import info
from spongify.forms import ArtistLoginForm


CreatorWaitlist = get_model(app_name="spongify", model_name="CreatorWaitlist")
User = get_model(app_name="accounts", model_name="User")


class HomeView(TemplateView):
    template_name = Templates.INDEX


home_view = HomeView.as_view()


class CreatorView(FormView):
    template_name = Templates.CREATOR_TEMPLATE
    form_class = ArtistLoginForm
    success_url = UrlPaths.HOME

    def form_valid(self, form):
        try:
            user = User.objects.get(**form.cleaned_data)
            info(
                request=self.request,
                message=AuthMessages.VERIFIED_ARTIST.format(
                    user=user.artist.stage_name
                ),
            )
        except User.artist.RelatedObjectDoesNotExist:
            form.add_error(None, AuthErrors.ARTIST_NOT_FOUND)
            return self.form_invalid(form)
        except User.DoesNotExist:
            form.add_error(None, AuthErrors.USER_NOT_FOUND)
            return self.form_invalid(form)
        return super().form_valid(form)


creator_view = CreatorView.as_view()


class CreatorJoinView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            info(request=request, message=AuthErrors.NOT_REGISTERED)
        else:
            if not CreatorWaitlist.objects.filter(user=request.user).exists():
                info(request=request, message=AuthMessages.CREATOR_REGISTRATION_JOINED)
                CreatorWaitlist.objects.create(user=request.user)
                artist_signup_mail_task.delay(self.request.user.id)
            info(request=request, message=AuthMessages.ALREADY_JOINED)
        return redirect(UrlPaths.CREATOR)


creator_join = CreatorJoinView.as_view()
