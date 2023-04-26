from django.contrib import admin

from .models import Menu, MenuItem


admin.site.register(Menu)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    search_fields = ('name',)
