from django.contrib import admin

from .models import *


class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tour, TourAdmin)
