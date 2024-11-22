from django.contrib import admin
from django.http import HttpRequest
from .models import (
    Category,
    Post,
    Comment,
    PostLike
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'parent',
    )
    ordering = ('-id',)
    list_filter = ('created_at', 'is_active',)
    search_fields = ('name',)
    list_editable = ('is_active',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'get_categories',
        'author',
        'is_active',
        'is_selected'
    )
    # list_editable = ('is_active', 'is_selected',)
    ordering = ('-id',)
    list_filter = ('published_at', 'categories',)
    search_fields = ('title', 'body', 'summary')

    def save_model(self, request: HttpRequest, obj: Post, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'author',
        'is_active',
        'parent',
    )
    ordering = ('id',)
    list_filter = ('created_at', 'is_active',)
    list_editable = ('is_active',)

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
    )
