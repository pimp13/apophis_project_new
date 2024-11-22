from django.views.generic import TemplateView
from content.models import Post
from course.models import Course
import random

class HomeView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_posts = Post.objects.filter(is_active=True, is_selected=True).all()
        num_posts = min(len(filtered_posts), 4)
        random_posts_slider = random.sample(list(filtered_posts), num_posts)
        latest_courses = Course.objects.filter(is_active=True).order_by('-id')[:8]
        context['random_posts_slider'] = random_posts_slider
        context['latest_courses'] = latest_courses
        return context
