from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# 博客文章model
class Article(models.Model):
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
