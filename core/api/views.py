from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.api.serializers import ArticleSerializer
from core.models import Article
from core.api import serializers
@api_view(['GET'])
def article_list_create_api_view(request):
    if request.method == 'GET':
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)