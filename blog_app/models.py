from django.contrib.auth.models import User
from django.db import models


# Blog Post Model.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Allows Modeled Data to show in Python Admin Panel
    def __str__(self):
        title = self.title
        return title
