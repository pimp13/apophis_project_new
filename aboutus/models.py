from django.db import models
from ckeditor.fields import RichTextField
from account.models import User

class AboutUs(models.Model):
    about_us = RichTextField('متن درباره ما:')
    user_admin = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کارشناسان',
    )
    is_main_aboutus = models.BooleanField(
        default=False,
        verbose_name='تنظیمات اصلی باشه؟'
    )

    def __str__(self):
        return "درباره مدافعان کبیر"

    class Meta:
        db_table = 'about_us'
        verbose_name = 'درباره مدافعان کبیر'
        verbose_name_plural = 'درباره ما'


