# Generated by Django 5.1.3 on 2024-11-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='content/posts/', verbose_name='تصویر'),
        ),
    ]
