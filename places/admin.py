from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Picture

admin.site.register(Picture)


class PictureInline(admin.TabularInline):
    model = Picture
    readonly_fields = ['preview_image']
    fields = ['image', 'preview_image', 'position']

    def preview_image(self, obj):
        return format_html(
            "<img src='{url}' height={height} />".format(
                url=obj.image.url,
                height=200
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline,
    ]
