# from django.conf import settings
from django.db import models
# from django.utils import timezone
from django.urls import reverse


class Menu(models.Model):
    '''
    Линейный список меню
    '''
    title = models.CharField(max_length=200, default='main')
    def get_url(self):
        return "/menu/%s/" % self.id
    def __str__(self):
        return self.title

class Parentmenu(models.Model):
    '''
    Структура меню
    '''
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    parent = models.ForeignKey(Menu, related_name='parent', on_delete=models.CASCADE, null=True, default='main')
    slug = models.SlugField(null=True)
    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.slug})
