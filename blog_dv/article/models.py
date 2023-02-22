from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from markdown import Markdown


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


class Avatar(models.Model):
    """标题图片"""
    content = models.ImageField(upload_to='avatar/%Y%m%d')

    class Meta:
        db_table = 'avatar'


class Article(models.Model):
    """博客 model"""
    title = models.CharField(verbose_name='标题', max_length=100)
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
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
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        return md_body, md.toc

    class Meta:
        db_table = 'article'
        ordering = ['-created']
