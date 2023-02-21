from django_filters import rest_framework as filters

from .models import Article


class ArticleFilter(filters.FilterSet):
    """
    自定义文章标题过滤器类，实现对文章标题进行模糊搜索(不区分大小写)
    """
    title = filters.CharFilter(field_name='title', lookup_expr='icontains', label='文章标题(模糊搜索且不区分大小写)')

    class Meta:
        model = Article
        fields = ['title']
