# Generated by Django 5.1.3 on 2024-11-17 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_videocategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocourse',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course.videocategory', verbose_name='دسته بندی ویدیو'),
        ),
    ]
