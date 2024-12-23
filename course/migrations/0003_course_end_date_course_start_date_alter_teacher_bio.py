# Generated by Django 5.1.3 on 2024-11-15 14:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_options_alter_enrollment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پایان'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ شروع دوره'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='بیوگرافی'),
        ),
    ]
