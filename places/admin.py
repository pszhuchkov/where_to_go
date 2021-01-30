from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Picture

admin.site.register(Picture)


class PictureInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    readonly_fields = ['preview_image']
    fields = ['image', 'preview_image']
    extra = 0

    def preview_image(self, obj):
        return format_html(
            "<img src='{url}' height={height} />".format(
                url=obj.image.url,
                height=200
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PictureInline]
    search_fields = ['title']
