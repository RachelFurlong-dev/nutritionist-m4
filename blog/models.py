from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_title = models.CharField(max_length=300, blank=False, null=False)
    slug = models.SlugField(max_length=50)
    body = models.TextField(blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(null=True, blank = True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.post_title