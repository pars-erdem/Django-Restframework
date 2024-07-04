from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.api.serializers import ArticleSerializer
from core.models import Article
from core.api import serializers
import requests

@api_view(['GET','POST'])
def article_list_create_api_view(request):
    if request.method == 'GET':
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def article_detail_api_view(request,pk):
    try:
        article_instance = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(
            {"error": "Resource not found", "message": f"Article with id {pk} does not exist.","code":404},
            status=status.HTTP_404_NOT_FOUND
        )
    ##GET
    if request.method == 'GET':
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    ##PUT
    elif request.method=='PUT':
        serializer = ArticleSerializer(data=request.data,instance=article_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        Response(status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method=='DELETE':
        article_instance.delete()
        return Response(
            { "message": f"{pk} id delete.", "code": 200},
            status=status.HTTP_200_OK
        )