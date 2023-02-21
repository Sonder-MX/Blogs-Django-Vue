from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        ordering = ['-created']


class Tag(models.Model):
    """文章标签"""
    text = models.CharField(verbose_name='文章标签', max_length=30)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'artag'
        ordering = ['-id']


class Article(models.Model):
    """博客 model"""
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    title = models.CharField(verbose_name='标题', max_length=100)
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        ordering = ['-created']
