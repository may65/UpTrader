from django.shortcuts import render

# Create your views here.
from menu.models import Menu, Parentmenu

def menu(request):
    slug = 'menu'
    menus = Menu.objects.all()
    parents = Parentmenu.objects.all()
    return render(request, 'menu/index.html', {'menus':menus, 'parents':parents, 'slug': slug})

def menu_slug(request, slug):
    parents = Parentmenu.objects.all()
    return render(request, 'menu/index.html', {'parents': parents, 'slug': slug})
