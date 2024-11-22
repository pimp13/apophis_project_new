from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailsView.as_view(), name='post_details'),
]

