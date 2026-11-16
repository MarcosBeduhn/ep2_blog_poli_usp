from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo')
    posted_at = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title
