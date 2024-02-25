from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Box(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxes'


class Messages(models.Model):
    chatbox = models.ForeignKey(Box, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
        verbose_name_plural = 'Messages'
