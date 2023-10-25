from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Article, Author, Comment
from .serializers import ArticleSerializer, AuthorSerializer, CommentSerializer


def homepage(request):
    return HttpResponse("This is a homepage")


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by("-id")
    serializer_class = ArticleSerializer


class ArticleAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().order_by("-id")
    serializer_class = ArticleSerializer


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer


class AuthorAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer


class CommentAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer
