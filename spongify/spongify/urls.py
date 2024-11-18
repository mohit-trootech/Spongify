from django.contrib import admin
from django.urls import path, include
from spongify.views import home_view
from spongify.constants import Reverse


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name=Reverse.HOME),
    path("accounts/", include("accounts.urls")),
]
