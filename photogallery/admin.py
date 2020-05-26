from django.contrib import admin
from .models import Image,Album,tags

class AlbumAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Image)
admin.site.register(Album,AlbumAdmin)
admin.site.register(tags)