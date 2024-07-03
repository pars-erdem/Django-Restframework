from django.contrib import admin
from django.urls import path,include
from core.api import views as api_views
urlpatterns = [
    path('articles/',api_views.article_list_create_api_view,name='article_list')
]