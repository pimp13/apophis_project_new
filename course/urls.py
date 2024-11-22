from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list'),
    path('<slug:slug>', views.CourseDetailsView.as_view(), name='course_details'),
    path('videos/<int:pk>', views.ShowVideoView.as_view(), name='show_videos'),
]

