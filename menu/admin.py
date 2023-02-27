from django.contrib import admin
from .models import *

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Parentmenu)
class ParentmenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'parent')
