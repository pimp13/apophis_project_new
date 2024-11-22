from datetime import datetime
from django.db import models
from django.utils.text import slugify
from account.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories', verbose_name='دسته بندی والد')
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
        db_table = 'categories'
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

class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='عنوان پست'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='اسلاگ',
        unique=True,
        allow_unicode=True,
        null=True,
        blank=True
    )
    body = RichTextField('متن اصلی:')
    summary = RichTextField('متن خلاصه:', null=True, blank=True)
    is_active = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='وضعیت',
        null=True,
        blank=True
    )
    view = models.IntegerField(
        default=1,
        verbose_name='بازدید ها'
    )
    is_selected = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='منتخب شده توسط سردبیر؟',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='content/posts/',
        verbose_name='تصویر'
    )
    categories = models.ManyToManyField(
        to=Category,
        related_name='posts',
        verbose_name='دسته بندی ها'
    )
    author = models.ForeignKey(
        to=User,
        related_name='author',
        related_query_name='author',
        verbose_name='نویسنده',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        editable=False
    )

    meta_title = models.CharField(
        max_length=120,
        verbose_name='عنوان متا در صفحه',
        null=True,
        blank=True
    )
    meta_description = models.TextField(
        max_length=230,
        verbose_name='توضیحات متا سئو',
        null=True,
        blank=True
    )
    meta_keywords = models.CharField(
        max_length=255,
        verbose_name='کلمات کلیدی با ویرگول , جدا شوند',
        null=True,
        blank=True
    )
    published_at = models.DateTimeField(default=datetime.now, verbose_name='تاریخ انتشار', null=True, blank=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')

    _metadata = {
        "title": "meta_title",
        "og_title": "meta_title",
        "twitter_title": "meta_title",
        "schemaorg_title": "title",
        "description": "meta_description",
        "og_description": "meta_description",
        "twitter_description": "meta_description",
        "schemaorg_description": "meta_description",
        "published_time": "created_at",
        "keywords": "meta_keywords",
        "image": "get_meta_image",
        "og_publisher": "created_at",
        # "image_object": None,
        # "image_width": False,
        # "image_height": False,
        # "object_type": get_setting("DEFAULT_TYPE"),
        # "og_type": get_setting("FB_TYPE"),
        # "og_app_id": get_setting("FB_APPID"),
        # "og_profile_id": get_setting("FB_PROFILE_ID"),
        # "og_author_url": get_setting("FB_AUTHOR_URL"),
        # "fb_pages": get_setting("FB_PAGES"),
        # "twitter_type": get_setting("TWITTER_TYPE"),
        # "twitter_site": get_setting("TWITTER_SITE"),
        # "twitter_author": get_setting("TWITTER_AUTHOR"),
        # "schemaorg_type": get_setting("SCHEMAORG_TYPE"),
        # "modified_time": False,
        # "expiration_time": False,
        # "tag": False,
        # "url": False,
        # "locale": False,
        # "custom_namespace": get_setting("OG_NAMESPACES"),
    }
    _schema = {
        'image': 'get_image_full_url',
        'articleBody': 'text',
        'articleSection': 'get_categories',
        'author': 'get_schema_author',
        'copyrightYear': 'copyright_year',
        'dateCreated': 'get_date',
        'dateModified': 'get_date',
        'datePublished': 'date_published',
        'headline': 'headline',
        'keywords': 'get_keywords',
        'description': 'get_description',
        'name': 'title',
        'url': 'get_full_url',
        'mainEntityOfPage': 'get_full_url',
        'publisher': 'get_site',
    }

    class Meta:
        db_table = 'posts'
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        unique_together = ['slug']

    def get_meta_image(self):
        if self.image:
            return self.image.url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.meta_title is None:
            self.meta_title = self.title
        if self.slug is None:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_categories(self):
        return [f"#{category.name}" for category in self.categories.select_related('parent').order_by('-id')[:4]]

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

class Comment(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', verbose_name='پاسخ به:', on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, verbose_name='پست مربوطه:', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده نظر', related_name='user_author')
    body = models.TextField(verbose_name='متن نظر')
    is_active = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ ویرایش')

    class Meta:
        db_table = 'comments'
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'توسط {self.author.username} : {self.content}'

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربران')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست ها')

    class Meta:
        db_table = 'posts_likes'
        verbose_name = 'لایک پست'
        verbose_name_plural = 'لایک های پست'
        unique_together = ('user', 'post')

    def __str__(self):
        return self.post.title
