from django.contrib import admin

from .models import *


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['nickname']}


admin.site.register(Song)
