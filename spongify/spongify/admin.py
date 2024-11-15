# Spongify Admin Panel

from django.contrib import admin
from utils.base_utils import get_model


EmailTemplate = get_model(app_name="spongify", model_name="EmailTemplate")


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ("subject", "choice", "is_html")
    search_fields = ("subject", "choice")
    list_filter = ("is_html",)
