# Generated by Django 5.1.3 on 2024-11-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_end_date_remove_course_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='تصویر شاخص'),
        ),
    ]