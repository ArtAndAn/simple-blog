from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True, editable=False)

    def short_article(self):
        return {'title': self.title,
                'category': str(self.category).title(),
                'author': str(self.author).title(),
                'created': self.created.strftime('%Y-%m-%d %H:%M'),
                'text': self.text,
                'slug': self.slug}

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
