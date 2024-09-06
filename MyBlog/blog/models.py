from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.published_date <= now