from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    # user = models.ForeignKey(User, related_name='forum_topic', on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # url = models.CharField(max_length=255, verbose_name="Post Name")
    def get_url(self):
        return "/menu/%s/" % self.id
    def __str__(self):
        return self.title

class Submenu(models.Model):
    """A forum
    >>> # Create a category
    >>> c = Category.objects.create(name='a')
    >>> c.save()
    >>> # Create a forum
    >>> f = Forum.objects.create(category=c, name='a', slug='a', description='a')
    >>> f.save()
    """
    title = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    def get_url(self):
        return "/submenu/%s/" % self.id
    def __str__(self):
        return self.title

