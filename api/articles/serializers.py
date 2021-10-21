from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Article


class ArticleFullSerializer(serializers.ModelSerializer):
    """Serializer for full articles data"""
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'category', 'created', 'slug')
