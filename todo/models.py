from django.db import models
from django.utils import timezone

class Post (models.Model):
    name = models.CharField(max_length=100)
    content =models.TextField(max_length=30000)
    created_at = models.DateField(default=timezone.now)


    def __str__(self):
        return self.name
