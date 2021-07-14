from django.shortcuts import render
from rest_framework import (
    viewsets,
)
from apps.blog.api.serializers import CategorySerializer
from apps.blog.models import Category
# Create your views here.

class CategoryListAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

