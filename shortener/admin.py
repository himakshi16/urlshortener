from django.contrib import admin
from .models import ShortURL, Visit


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code','original_url','created_by','created_at')


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('short','ip','timestamp')
