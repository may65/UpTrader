# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

@admin.register(Menu)
class ForumAdmin(admin.ModelAdmin):
    pass
    list_display = ('title',)

@admin.register(Submenu)
class ForumAdmin(admin.ModelAdmin):
    pass
    list_display = ('title','menu')
