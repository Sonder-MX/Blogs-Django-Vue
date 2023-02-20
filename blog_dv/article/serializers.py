from rest_framework import serializers
from user_info.serializers import UserDescSerializer
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    # 实现超链接可以用 DRF 框架提供的 HyperlinkedIdentityField
    url = serializers.HyperlinkedIdentityField(view_name='article:detail')
    author = UserDescSerializer(read_only=True)  # 只读

    class Meta:
        model = Article
        fields = ['url', 'title', 'body', 'author']
        # read_only_fields = ['author']


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
