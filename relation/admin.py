from django.contrib import admin

# Register your models here.
from relation.models import Singer,Song

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']