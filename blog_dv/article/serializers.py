from rest_framework import serializers
from user_info.serializers import UserDescSerializer
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    author = UserDescSerializer(read_only=True)  # 只读

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'author']
        # read_only_fields = ['author']


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
