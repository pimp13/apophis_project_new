# Generated by Django 5.1.3 on 2024-11-14 11:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن خلاصه:'),
        ),
    ]
