from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = models.TextField(blank=True, null=True, verbose_name='текст')
    count_like = models.PositiveIntegerField(default=0, verbose_name='лайки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_post')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['count_like']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    count_like = models.PositiveIntegerField(default=0, verbose_name='лайки')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_comment')

    def __str__(self):
        return self.post.title + ' ' + self.text


