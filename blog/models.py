from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} from {self.author}'

    def get_absolute_url(self):
        return reverse('blog/post_detail', args=[ str(self.id) ])
