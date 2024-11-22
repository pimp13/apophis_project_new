from django.db import models
from account.models import User

class Menu(models.Model):
    title = models.CharField(max_length=191, verbose_name='عنوان منو')
    url = models.URLField(verbose_name='آدرس URL')
    is_active = models.BooleanField(verbose_name='وضعیت', db_index=True, default=False)
    icon = models.CharField(max_length=100, verbose_name='آیکون منو', null=True, blank=True)

    class Meta:
        db_table = 'menus'
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'

    def __str__(self):
        return self.title

class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenus', related_query_name='submenu', on_delete=models.CASCADE, verbose_name='منوی والد')
    title = models.CharField(max_length=191, verbose_name='عنوان زیر منو')
    url = models.URLField(verbose_name='آدرس URL')
    icon = models.CharField(max_length=100, verbose_name='آیکون منو', null=True, blank=True)

    class Meta:
        db_table = 'sub_menus'
        verbose_name = 'زیر منو'
        verbose_name_plural = 'زیر منو ها'

    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=191, verbose_name='نام سایت')
    site_url = models.URLField(max_length=255, verbose_name='آدرس سایت')
    meta_description = models.TextField(verbose_name='توضیحات سایت')
    site_author = models.ForeignKey(
        User,
        verbose_name='نویسنده سایت',
        related_name='user',
        on_delete=models.CASCADE
    )
    site_lang = models.CharField(max_length=100, verbose_name='زبان سایت')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی؟');
    site_logo = models.ImageField(upload_to='images/', verbose_name='لوگوی سایت')
    site_favicon = models.ImageField(upload_to='images/', verbose_name='آیکون Favicon', null=True, blank=True)
    site_email = models.EmailField(unique=True, verbose_name='ایمیل سایت', blank=True, null=True)
    copyright = models.TextField(verbose_name='متن کپی رایت', max_length=500)

    class Meta:
        db_table = 'site_settings'
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name
