from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
from .forms import PostFilterForm

class PostListView(ListView):
    model = Post
    template_name = 'content/post-list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.all()
        form = PostFilterForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data['search']:
                query = form.cleaned_data['search']
                queryset = queryset.filter(title__icontains=query) | queryset.filter(meta_description__icontains=query)

            category_ids = self.request.GET.getlist('category')
            if category_ids:
                queryset = queryset.filter(categories__id__in=category_ids).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostFilterForm(self.request.GET)
        context['categories'] = Category.objects.all()
        return context

    def is_htmx_request(self):
        return self.request.headers.get('HX-Request') is not None

    def render_to_response(self, context, **response_kwargs):
        if self.is_htmx_request():
            return render(self.request, 'content/components/post-list-partial.html', context)
        return super().render_to_response(context, **response_kwargs)

class PostDetailsView(DetailView):
    model = Post
    template_name = 'content/post-details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
