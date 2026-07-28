from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('sports', 'Sports'),
        ('politics', 'Politics'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title