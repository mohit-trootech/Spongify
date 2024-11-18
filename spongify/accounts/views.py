from django.views.generic import FormView
from accounts.forms import (
    RegisterForm,
    LoginForm,
    PasswordResetForm,
    PasswordResetDoneForm,
)
from django.contrib.messages import info
from django.contrib.auth import authenticate, login, logout
from utils.base_utils import get_model
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse_lazy
from django.views import View
from accounts.tasks import (
    password_reset_mail,
    password_reset_done as password_reset_done_mail,
)
from accounts.constants import AuthErrors, AuthMessages, Templates, UrlPaths

User = get_model(app_name="accounts", model_name="User")


class RegisterView(FormView):
    template_name = Templates.REGISTER
    form_class = RegisterForm
    success_url = UrlPaths.REGISTER
    success_message = AuthMessages.REGISTER_SUCCESS

    def form_valid(self, form):
        try:
            if self.request.POST["password"] != self.request.POST["confirm_password"]:
                form.add_error(None, AuthErrors.PASSWORD_MISMATCH)
                return super().form_invalid(form)
            validate_password(self.request.POST["password"])
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            info(self.request, self.success_message)
            return super().form_valid(form)
        except Exception as err:
            form.add_error(None, err)
            return super().form_invalid(form)


register_view = RegisterView.as_view()


class LoginView(FormView):
    template_name = Templates.LOGIN
    form_class = LoginForm
    success_url = UrlPaths.HOME
    success_message = AuthMessages.LOGIN_SUCCESS

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            form.add_error(None, AuthErrors.INVALID_USERNAME_PASSWORD)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, self.success_message)
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(View):
    def get(self):
        logout(self.request)
        info(self.request, AuthMessages.LOGOUT_SUCCESS)
        return reverse_lazy("accounts:login")


logout_view = LogoutView.as_view()


class PasswordResetView(FormView):
    template_name = Templates.PASSWORD_RESET
    form_class = PasswordResetForm
    success_url = UrlPaths.PASSWORD_RESET_DONE
    success_message = AuthMessages.PASSWORD_RESET_OTP_SENT

    def form_valid(self, form):
        try:
            user = User.objects.get(email=form.cleaned_data["email"])
        except User.DoesNotExist:
            form.add_error(None, AuthErrors.EMAIL_NOT_FOUND)
            return super().form_invalid(form)
        password_reset_mail.delay(id=user.id)
        info(self.request, self.success_message)
        self.request.session["email"] = form.cleaned_data["email"]
        return super().form_valid(form)


password_reset = PasswordResetView.as_view()


class PasswordResetDone(FormView):
    template_name = Templates.PASSWORD_RESET_DONE
    form_class = PasswordResetDoneForm
    success_url = UrlPaths.LOGIN
    success_message = AuthMessages.OTP_VERIFIED_SUCCESSFULLY

    def form_valid(self, form):
        if not self.request.session.has_key("email"):
            form.add_error(None, AuthErrors.SESSION_EXPIRED)
            return super().form_invalid(form)
        email = self.request.session.get("email")
        try:
            user = User.objects.get(email=email)
            otp = "".join([*form.cleaned_data.values()])
            if otp != user.otp.otp:
                form.add_error(None, AuthErrors.INVALID_OTP)
            if (
                not self.request.POST["password"]
                == self.request.POST["confirm_password"]
            ):
                form.add_error(None, AuthErrors.PASSWORD_MISMATCH)
                return super().form_invalid(form)
            validate_password(self.request.POST["password"])
            if user.otp.is_expired:
                form.add_error(None, AuthErrors.OTP_EXPIRED)
                return super().form_invalid(form)
            user.set_password(self.request.POST["password"])
            user.save()
            logout(self.request)
            info(self.request, AuthMessages.OTP_VERIFIED_SUCCESSFULLY)
            password_reset_done_mail.delay(id=user.id)
            return super().form_valid(form)
        except User.DoesNotExist:
            form.add_error(None, AuthErrors.EMAIL_NOT_FOUND)
            return super().form_invalid(form)
        except Exception as err:
            form.add_error(None, err)
            return super().form_invalid(form)


password_reset_done = PasswordResetDone.as_view()
