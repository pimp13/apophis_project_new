from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.sites.shortcuts import get_current_site
from setting.models import Menu

def meta_tags_component(request: HttpRequest):
    current_site = get_current_site(request)
    canonical_url = request.build_absolute_uri(request.path)
    context = {'canonical_url': canonical_url}
    return render(request, 'components/_metatags.html', context)

def header_component(request: HttpRequest):
    menus: Menu = Menu.objects.filter(is_active=True).all()
    context = {'menus': menus}
    return render(request, 'base/components/_header.html', context)

def footer_component(request: HttpRequest):
    context = {}
    return render(request, 'base/components/_footer.html', context)
