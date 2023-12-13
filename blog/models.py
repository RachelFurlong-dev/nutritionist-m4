from django.db import models
from django.contrib.auth.models import User

# Define possible statuses for a Post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    # Define fields for the Post model
    post_title = models.CharField(max_length=300, blank=False, null=False)
    slug = models.SlugField(max_length=50)
    body = models.TextField(blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
            User, on_delete=models.CASCADE, blank=False, null=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # Set the default ordering for the model
        ordering = ['-publish_date']

    def __str__(self):
        # String representation of a Post object
        return self.post_title

    def save(self, *args, **kwargs):
        # Generate a slug if it doesn't exist
        if not self.slug:
            self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)
