from django.urls import path
from accounts.views import (
    register_view,
    login_view,
    password_reset,
    logout_view,
    password_reset_done,
    profile_view,
)
from accounts.constants import Reverse

app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name=Reverse.REGISTER),
    path("login/", login_view, name=Reverse.LOGIN),
    # TODO: Add session based force logout with signal to automatically logout from all devices
    # path("force-logout", force_logout_view, name=Reverse.FORCE_LOGOUT),
    path("login/", login_view, name=Reverse.LOGIN),
    path("logout/", logout_view, name=Reverse.LOGOUT),
    path("profile/<str:username>", profile_view, name=Reverse.PROFILE),
    # TODO: Add verify token view to handle user account verification
    # path("verify/<str:token>/", views.VerifyView.as_view(), name="verify"),
    path("password-reset/", password_reset, name=Reverse.PASSWORD_RESET),
    path("password-reset-done/", password_reset_done, name=Reverse.PASSWORD_RESET_DONE),
]
