from django.contrib import admin

from . import models


class NewsAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    fields = ('name',
              'description',
              'tags',
              'created_at',
              )


class TagAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.News, NewsAdminModel)
admin.site.register(models.Tag, TagAdminModel)
