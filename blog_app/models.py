from django.contrib.auth.models import User
from django.db import models


# Blog Post Model.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    post_excerpt = models.TextField(max_length=255, blank=True)
    featured_image = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Allows Modeled Data to show in Python Admin Panel
    def __str__(self):
        return self.title
