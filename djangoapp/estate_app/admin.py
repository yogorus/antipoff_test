from django.contrib import admin
from .models import CadastralRequest


# Register your models here.
class CadastralRequestAdmin(admin.ModelAdmin):
    search_fields = ["cadastral_number"]
    list_display = ["cadastral_number", "latitude", "longitude", "status", "date"]


admin.site.register(CadastralRequest, CadastralRequestAdmin)
