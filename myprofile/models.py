from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Profilepost(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def get_self_url(self):
        return reverse('profilepost', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title