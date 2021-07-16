from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()