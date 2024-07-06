from django.contrib import admin
from django.urls import path,include
from core.api import views as api_views
urlpatterns = [
    path('articles/',api_views.ArticleListView.as_view(),name='article_list'),
    path('journals/',api_views.JournalArticleListView.as_view(),name='journal_article_list'),
    path('articles/<int:pk>/', api_views.ArticleDetailView.as_view(), name='article_detail'),

]