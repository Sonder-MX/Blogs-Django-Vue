from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from article.models import Article


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )
    content = models.TextField(verbose_name='评论')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20]

    class Meta:
        db_table = 'comment_db'
        ordering = ['-created']
