from django.contrib import admin
from .models import *


class HoteListAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "description", "check_in", "check_out")
admin.site.register(Hotels, HoteListAdmin)


