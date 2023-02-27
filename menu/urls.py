from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<slug:slug>', views.menu_slug, name='menu'),
]
