from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'get_full_name',
        'email',
        'is_active',
        'last_login'
    )
