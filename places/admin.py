from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']


class PictureInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    readonly_fields = ['get_preview_image']
    fields = ['image', 'get_preview_image']
    extra = 0

    def get_preview_image(self, obj):
        if not obj.image:
            return "Здесь будет превью, когда файл загрузится"
        return format_html("<img src='{}' height=200 />", obj.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PictureInline]
    search_fields = ['title']
