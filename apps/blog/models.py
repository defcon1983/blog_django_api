from django.db import models
from django.db.models.fields import AutoField, BooleanField, DateField, TextField
# importacion del user del propio django
from .managers import CategoryManager
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    objects = CategoryManager()

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True, help_text='titulo')
    imagen = models.ImageField(upload_to='blog')
    content = models.TextField()
    idAutor = models.ForeignKey(User, related_name='usuarios', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    publish = models.BooleanField()
    categories = models.ManyToManyField(Category, related_name='blogs')


    def __str__(self):
        return self.title