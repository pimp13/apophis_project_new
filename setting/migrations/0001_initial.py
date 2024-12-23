# Generated by Django 5.1.3 on 2024-11-14 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191, verbose_name='عنوان منو')),
                ('url', models.URLField(verbose_name='آدرس URL')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'منو',
                'verbose_name_plural': 'منو ها',
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=191, verbose_name='نام سایت')),
                ('site_url', models.URLField(max_length=255, verbose_name='آدرس سایت')),
                ('meta_description', models.TextField(verbose_name='توضیحات سایت')),
                ('site_lang', models.CharField(max_length=100, verbose_name='زبان سایت')),
                ('is_main_setting', models.BooleanField(default=False, verbose_name='تنظیمات اصلی؟')),
                ('site_logo', models.ImageField(upload_to='images/', verbose_name='لوگوی سایت')),
                ('site_favicon', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='آیکون Favicon')),
                ('site_email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='ایمیل سایت')),
                ('copyright', models.TextField(max_length=500, verbose_name='متن کپی رایت')),
                ('site_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
                'db_table': 'site_settings',
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191, verbose_name='عنوان زیر منو')),
                ('url', models.URLField(verbose_name='آدرس URL')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenus', related_query_name='submenu', to='setting.menu', verbose_name='منوی والد')),
            ],
            options={
                'verbose_name': 'زیر منو',
                'verbose_name_plural': 'زیر منو ها',
                'db_table': 'sub_menus',
            },
        ),
    ]
