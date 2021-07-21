from django.db.models.fields import PositiveBigIntegerField
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
    

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Blog
        fields = (
            'title',
            'imagen',
            'content',
            'idAutor',
            'created_at',
            'updated_at',
            'views',
            'like',
            'dislike',
            'publish',
            'categories',
        )
    


