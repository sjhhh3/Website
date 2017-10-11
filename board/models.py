from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=140)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.author

