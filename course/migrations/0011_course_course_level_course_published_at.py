# Generated by Django 5.1.3 on 2024-11-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_remove_videocourse_category_delete_videocategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_level',
            field=models.CharField(choices=[('easy-to-hard', 'مقدماتی تا پیشرفته'), ('easy', 'آسان مقدماتی'), ('medium', 'متوسط'), ('hard', 'پیشرفته سخت')], default='easy-to-hard', max_length=100, verbose_name='سطح دوره'),
        ),
        migrations.AddField(
            model_name='course',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
