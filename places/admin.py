from django.contrib import admin
from places.models import Place, Picture


admin.site.register(Picture)


class PictureInline(admin.TabularInline):
    model = Picture


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline,
    ]



