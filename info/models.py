from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=500)
    intro = models.CharField(max_length=2000)
    text = models.TextField(max_length=20000)
    slug = models.SlugField(max_length=500)
    published = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title