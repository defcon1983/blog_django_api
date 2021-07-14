from rest_framework import serializers
from apps.blog.models import (
    Category,
    Blog,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'name']
        fields = '__all__'
        #exclude = ('content', 'title')