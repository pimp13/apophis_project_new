# Generated by Django 5.1.3 on 2024-11-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='آیکون منو'),
        ),
        migrations.AddField(
            model_name='submenu',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='آیکون منو'),
        ),
    ]
