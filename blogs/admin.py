from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug":()}


admin.site.register(models.Entry, EntryAdmin)