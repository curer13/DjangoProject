from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='the_user')
    topic = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    date = models.DateField(default=timezone.now)
    comment = models.CharField('Комментарий', max_length=100, default='Комментарий')
    # slug = models.SlugField(max_length=200, unique=True, default='default')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return  reverse('home')
        #return reverse('article-detail', args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Comment {self.body} created by {self.name}'
