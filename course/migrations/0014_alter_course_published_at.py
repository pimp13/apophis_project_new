# Generated by Django 5.1.3 on 2024-11-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_alter_course_meta_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار'),
        ),
    ]