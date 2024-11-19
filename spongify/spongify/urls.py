from django.contrib import admin
from django.urls import path, include
from spongify.views import home_view
from spongify.constants import Reverse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name=Reverse.HOME),
    path("accounts/", include("accounts.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Spongify Admin"
