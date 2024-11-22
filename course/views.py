from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, CourseCategory, VideoCourse
from .forms import CourseFilterForm

class CourseListView(ListView):
    model = Course
    template_name = 'course/index.html'
    context_object_name = 'courses'
    ordering = ('-created_at')
    paginate_by = 9

    def get_queryset(self):
        queryset = Course.objects.all()
        form = CourseFilterForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data['search']:
                query = form.cleaned_data['search']
                queryset = queryset.filter(title__icontains=query) | queryset.filter(short_description__icontains=query)

        category_ids = self.request.GET.getlist('category')
        if category_ids:
            queryset = queryset.filter(categories__id=category_ids).all()

        price_filter = self.request.GET.get('price')
        if price_filter == 'free':
            queryset = queryset.filter(course_status=Course.FREE).all()
        elif price_filter == 'paid':
            queryset = queryset.filter(course_status=Course.PAID).all()
        elif price_filter == 'all':
            queryset = queryset.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CourseFilterForm(self.request.GET)
        context['categories'] = CourseCategory.objects.all()
        return context

    def is_htmx_request(self):
        return self.request.headers.get('HX-Request') is not None

    def render_to_response(self, context, **response_kwargs):
        if self.is_htmx_request():
            return render(self.request, 'course/components/course-list-partial.html', context)
        return super().render_to_response(context, **response_kwargs)

class CourseDetailsView(DetailView):
    model = Course
    template_name = 'course/course-details.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro_video_course'] = self.object.videos.first()
        return context


class ShowVideoView(DetailView):
    model = VideoCourse
    template_name = 'course/show-videos.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
