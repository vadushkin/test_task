from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="post")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
