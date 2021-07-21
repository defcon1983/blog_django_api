from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from rest_framework import (
    viewsets,
)
from rest_framework.generics import ListAPIView
from apps.blog.api.serializers import CategorySerializer, BlogSerializer
from apps.blog.models import Category, Blog
# Create your views here.


class CategoryListAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.list_category()


class BlogListAPIView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
