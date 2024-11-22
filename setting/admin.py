from django.contrib import admin
from .models import (Menu, SubMenu, SiteSetting)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_active')

@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'menu')


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'site_url',
        'site_author',
        'is_main_setting'
    )