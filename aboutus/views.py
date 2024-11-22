from django.views.generic import TemplateView
from .models import AboutUs

class AboutUsView(TemplateView):
    template_name = ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.select_related('user_admin').filter(is_main_aboutus=True).first()
        return context