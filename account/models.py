from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_photo_path = models.ImageField(
        upload_to='images/',
        verbose_name='تصویر پروفایل',
        null=True,
        blank=True,
        default='/static/images/avatar_user.png'
    )
    email_active_code = models.CharField(max_length=120, verbose_name='توکن فعال سازی کاربر', blank=True, null=True)

    class Meta:
        db_table = "users"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        if self.first_name == '' and self.last_name == '':
            return self.username
        else:
            return self.get_full_name()
