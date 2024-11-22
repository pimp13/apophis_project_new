from django.contrib import admin
from django.http import HttpRequest
from . import models

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio',
    )

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'teacher',
        'course_type',
        'is_active'
    )
    ordering = ('-id',)
    list_editable = ('is_active',)
    search_fields = ('title', 'meta_description', 'meta_keywords', 'short_description')
    list_filter = ('published_at', 'course_status', 'course_level')

@admin.register(models.VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'title',
    )

@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'course',
    )

@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'user',
        'score'
    )

@admin.register(models.CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'parent'
    )

@admin.register(models.CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
    )
    list_editable = ('is_active',)
