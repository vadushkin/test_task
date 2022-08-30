from django.contrib import admin

from . import models


class NewsAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',), }
    fields = ('name',
              'slug',
              'description',
              'created_at',
              )
    readonly_fields = ('created_at',)


class TagAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.News, NewsAdminModel)
admin.site.register(models.Tag, TagAdminModel)
