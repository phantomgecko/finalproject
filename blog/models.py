from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title