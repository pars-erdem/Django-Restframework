from django.db import models
# Create your models here.

class Journalist(models.Model):
    name = models.CharField(max_length=254)
    bio = models.TextField(verbose_name="Bio",default='')
    def __str__(self):
        return self.name
class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE,related_name='articles')
    title = models.CharField(max_length=254,verbose_name='title')
    text = models.TextField(verbose_name='text')
    city = models.CharField(max_length=100,verbose_name='city')
    creation_date = models.DateTimeField(auto_now_add=True,verbose_name='creation date')
    update_date = models.DateTimeField(auto_now=True,verbose_name='update date')
    publish_date = models.DateTimeField(blank=True, null=True,verbose_name='publish date')
    active = models.BooleanField(default=True,verbose_name='active')
    def __str__(self):
        return self.title