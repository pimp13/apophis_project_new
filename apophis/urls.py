from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('content/', include('content.urls')),
    path('courses/', include('course.urls')),
    path('', include('base.urls')),
    path('', include('aboutus.urls')),
    path('', include('account.urls')),
]

urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
