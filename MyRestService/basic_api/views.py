from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basic_api.models import Article
from basic_api.serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Full list':'/article',
        'list with filter': '/article/<str:title>/',
        'create':'/article-add/',
        'update':'/article-update/<str:title>',
        'delete':'/article-delete/<str:title>'
    }
    return Response(api_urls)

@api_view(['GET'])
def getArticleList(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getArticleDetail(request,title_name):
    article = Article.objects.get(title=title_name)
    serializer = ArticleSerializer(article,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateArticle(request,title_name):
    article = Article.objects.get(title=title_name)
    serializer = ArticleSerializer(instance=article,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteArticle(request,title_name):
    article = Article.objects.get(title=title_name)
    article.delete()
    return Response("Item Successfully deleted!")
