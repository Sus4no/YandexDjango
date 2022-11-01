from django.contrib import admin
from .models import catalog_tag, catalog_category, catalog_item


admin.site.site_header = 'Администрирование Django'
admin.site.index_title = 'Администрация сайта'


@admin.register(catalog_item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )
    filter_horizontal = ('tags', )


@admin.register(catalog_tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )


@admin.register(catalog_category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )
