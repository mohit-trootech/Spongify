from django.urls import path
from accounts.views import (
    register_view,
    login_view,
    password_reset,
    logout_view,
    password_reset_done,
)
from accounts.constants import Reverse

app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name=Reverse.REGISTER),
    path("login/", login_view, name=Reverse.LOGIN),
    path("logout/", logout_view, name=Reverse.LOGOUT),
    # path("profile/", views.ProfileView.as_view(), name="profile"),
    # path("verify/<str:token>/", views.VerifyView.as_view(), name="verify"),
    path("password-reset/", password_reset, name=Reverse.PASSWORD_RESET),
    path("password-reset-done/", password_reset_done, name=Reverse.PASSWORD_RESET_DONE),
    # path(
    #     "password-reset/confirm/<str:token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password-reset-confirm",
    # ),
]
