# Generated by Django 5.1.3 on 2024-11-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_post_meta_description_post_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
