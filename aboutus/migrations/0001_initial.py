# Generated by Django 5.1.3 on 2024-11-14 10:05

import ckeditor.fields
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
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', ckeditor.fields.RichTextField(verbose_name='متن درباره ما:')),
                ('is_main_aboutus', models.BooleanField(default=False, verbose_name='تنظیمات اصلی باشه؟')),
                ('user_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کارشناسان')),
            ],
            options={
                'verbose_name': 'درباره مدافعان کبیر',
                'verbose_name_plural': 'درباره ما',
                'db_table': 'about_us',
            },
        ),
    ]
