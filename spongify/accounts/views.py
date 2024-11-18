from django.views.generic import FormView, TemplateView
from django.views.generic.edit import FormMixin
from accounts.forms import RegisterForm, LoginForm, PasswordResetForm
from django.contrib.messages import info
from django.contrib.auth import authenticate, login, logout
from utils.base_utils import get_model
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse_lazy
from django.views import View
from accounts.tasks import password_reset_mail

User = get_model(app_name="accounts", model_name="User")


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = "/accounts/login/"
    success_message = "Registered successfully"

    def form_valid(self, form):
        try:
            if self.request.POST["password"] != self.request.POST["confirm_password"]:
                form.add_error(None, "Passwords do not match")
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
    template_name = "accounts/login.html"
    form_class = LoginForm
    success_url = "/"
    success_message = "Login successfully"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            form.add_error(None, "Invalid username or password")
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, self.success_message)
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(View):
    def get(self):
        logout(self.request)
        info(self.request, "Logged out successfully")
        return reverse_lazy("accounts:login")


logout_view = LogoutView.as_view()


class PasswordResetView(FormView):
    template_name = "accounts/password_reset.html"
    form_class = PasswordResetForm
    success_url = "/accounts/password-reset-done/"
    success_message = "Password reset otp sent to your email"

    def form_valid(self, form):
        try:
            User.objects.get(email=form.cleaned_data.get("email"))
        except User.DoesNotExist:
            form.add_error(None, "Email does not exist")
            return super().form_invalid(form)
        password_reset_mail.delay(email=form.cleaned_data.get("email"))
        info(self.request, self.success_message)
        return super().form_valid(form)


password_reset = PasswordResetView.as_view()


class PasswordResetDone(TemplateView):
    template_name = "accounts/password_reset_done.html"

    def form_valid(self, form):
        breakpoint()
        form
        return super().form_valid(form)


password_reset_done = PasswordResetDone.as_view()
