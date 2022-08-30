from django.contrib import admin

from . import models


class NewsAdminModel(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name', 'description')
    fields = ('name',
              'description',
              'created_at',
              )
    readonly_fields = ('created_at',)


class TagAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.News)
admin.site.register(models.Tag, TagAdminModel)
