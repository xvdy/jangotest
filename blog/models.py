from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128, help_text="标题")
    author = models.CharField(max_length=16)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now=True)
