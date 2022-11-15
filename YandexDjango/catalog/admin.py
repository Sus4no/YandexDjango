from django.contrib import admin
from .models import Tag, Category, Item, Gallery


admin.site.site_header = 'Администрирование Django'
admin.site.index_title = 'Администрация сайта'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tmb')


class GalleryInline(admin.TabularInline):
    model = Gallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb')
    list_editable = ('is_published', )
    list_display_links = ('name', )
    filter_horizontal = ('tags', )
    inlines = (GalleryInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )
