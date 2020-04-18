from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #dinamik url icin reverse
        return reverse('post:detail', kwargs={'id': self.id})
       # return "/post/{}".format(self.id)
