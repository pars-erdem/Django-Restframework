from django.contrib import admin

# Register your models here.
from django.contrib import admin
from core.models import Article,Journalist
# Register your models here.
admin.site.register(Article)
admin.site.register(Journalist)