from django.db import models
from account.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import Sum
from datetime import timedelta, datetime

class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        db_table = 'students'
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'

    def __str__(self):
        return self.user.__str__()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    bio = RichTextField(blank=True, null=True, verbose_name='بیوگرافی')

    class Meta:
        db_table = 'teachers'
        verbose_name = 'مدرس'
        verbose_name_plural = 'مدرسان'

    def __str__(self):
        return self.user.get_full_name()

class CourseCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories', verbose_name='دسته بندی والد')
    name = models.CharField(
        max_length=255,
        verbose_name='نام دسته بندی'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='اسلاگ',
        unique=True,
        allow_unicode=True,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='وضعیت'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')

    class Meta:
        db_table = 'course_categories'
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_posts', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

class CourseTag(models.Model):
    name = models.CharField(max_length=191, verbose_name='نام تگ')
    slug = models.SlugField(
        max_length=255,
        verbose_name='اسلاگ',
        unique=True,
        allow_unicode=True,
        db_index=True
    )
    is_active = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='وضعیت'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')
    class Meta:
        db_table = 'course_tags'
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category_posts', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

class Course(models.Model):
    FREE = 'free'
    PAID = 'paid'
    COURSE_TYPE_CHOICES = [
        (FREE, 'رایگان'),
        (PAID, 'غیر رایگان'),
    ]

    IN_PROGRESS = 'in-progress'
    ENDED = 'ended'
    NO_STARTED = 'no-started'
    COURSE_STATUS = [
        (IN_PROGRESS, 'در حال برگزاری...'),
        (ENDED, 'به اتمام رسیده'),
        (NO_STARTED, 'هنوز شروع نشده'),
    ]

    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    EASY_TO_HARD = 'easy-to-hard'
    COURSE_LEVEL = [
        (EASY_TO_HARD, 'مقدماتی تا پیشرفته'),
        (EASY, 'آسان مقدماتی'),
        (MEDIUM, 'متوسط'),
        (HARD, 'پیشرفته سخت'),
    ]

    title = models.CharField(
        verbose_name='عنوان دوره',
        max_length=191
    )
    slug = models.SlugField(
        max_length=191,
        verbose_name='اسلاگ',
        unique=True,
        allow_unicode=True,
        null=True,
        blank=True
    )
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE, verbose_name='مدرس دوره')
    students = models.ManyToManyField(Student, through='Enrollment', related_name='courses', verbose_name='دانشجویان')
    category = models.ForeignKey(CourseCategory, related_name='courses', on_delete=models.CASCADE, verbose_name='دسته بندی', null=True, blank=True)
    tags = models.ManyToManyField(CourseTag, related_name='courses', verbose_name='برچسب ها')
    price = models.DecimalField(
        verbose_name='قیمت دوره',
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=3
    )
    meta_description = models.TextField(verbose_name='توضیحات متا', null=True, blank=True)
    short_description = RichTextField('توضیحات دوره')
    meta_title = models.CharField(max_length=191, verbose_name='عنوان سئو', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/',
        verbose_name='تصویر شاخص',
        null=True,
        blank=True
    )
    course_type = models.CharField(
        max_length=15,
        choices=COURSE_TYPE_CHOICES,
        default=PAID,
        verbose_name='نوع ویدیو'
    )
    course_level = models.CharField(
        max_length=100,
        choices=COURSE_LEVEL,
        default=EASY_TO_HARD,
        verbose_name='سطح دوره'
    )
    course_status = models.CharField(
        max_length=15,
        choices=COURSE_STATUS,
        default=NO_STARTED,
        verbose_name='وضعیت برگزاری دوره'
    )
    meta_keywords = models.CharField(
        max_length=255,
        verbose_name='کلمات کلیدی با ویرگول , جدا شوند',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(verbose_name='وضعیت دوره فعال بودن', default=True, db_index=True)
    published_at = models.DateTimeField(default=datetime.now, verbose_name='تاریخ انتشار', null=True, blank=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')

    class Meta:
        db_table = 'courses'
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    @property
    def sum_rating(self):
        ratings = self.ratings.all()
        if ratings:
            return sum(rating.score for rating in ratings) / len(ratings)
        return 0

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return ratings.aggregate(models.Avg('score'))['score__avg']
        return 0

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_details', kwargs={'slug': self.slug})

    @property
    def total_duration(self):
        total_minutes = self.videos.aggregate(models.Sum('duration_in_minutes'))['duration_in_minutes__sum'] or 0
        return f"{total_minutes} دقیقه" if total_minutes else "No videos"

    @property
    def total_videos(self):
        return f"{self.videos.count() | 0} ویدیو"

    @property
    def all_tags(self):
        return self.tags.filter(is_active=True)

class VideoCourse(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    title = models.CharField(max_length=255, verbose_name='عنوان ویدیو')
    description = models.TextField(verbose_name='توضیحات کوتاه')
    video_url = models.URLField(verbose_name='لینک ویدیو')  # برای ذخیره URL ویدیو
    duration_in_minutes = models.PositiveIntegerField(verbose_name='تایم ویدیو')  # مدت زمان ویدیو به دقیقه
    order = models.PositiveIntegerField(verbose_name='شماره جلسه ویدیو')  # ترتیب ویدیوها در دوره

    class Meta:
        db_table = 'video_courses'
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو های دوره'

    def __str__(self):
        return f'{self.title} - {self.course.title}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)  # مشخص می‌کند که دانشجو دوره را تکمیل کرده است یا نه

    def __str__(self):
        return f'{self.student} - {self.course}'

    class Meta:
        db_table = 'enrollments'
        verbose_name = 'دانشجوی دوره'
        verbose_name_plural = 'دانشجویان دوره ها'

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings', verbose_name='دوره')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='کاربر')
    score = models.DecimalField(
        max_digits=3, decimal_places=1,
        choices=[(i / 2, i / 2) for i in range(2, 11)],
        verbose_name='امتیاز'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_rating'
        verbose_name = 'امتیاز'
        verbose_name_plural = 'امتیاز دهی'
        unique_together = ('course', 'user')  # هر کاربر فقط یکبار می‌تواند امتیاز بدهد

    def __str__(self):
        return f"{self.user.username} rated {self.course.title} with {self.score}"
