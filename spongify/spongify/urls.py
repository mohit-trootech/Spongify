from django.contrib import admin
from django.urls import path, include
from spongify.constants import Reverse
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from spongify.views import creator_join, creator_view, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name=Reverse.HOME),
    path("creator/", creator_view, name=Reverse.CREATOR),
    path("creator/join/", creator_join, name=Reverse.CREATOR_JOIN),
    path("creator/", include("music.urls")),
    path("accounts/", include("accounts.urls")),
] + debug_toolbar_urls()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Spongify Admin"
