from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def get_next_url(self):
        #try:
            #Post.objects.get(pk=self.pk+1)
            #return reverse('blog:post', kwargs={'pk':self.pk+1})
            #return Post.objects.latest('date')
            #return Post.objects.latest('date').pk
        #except ObjectDoesNotExist:
        max = Post.objects.latest('date').pk
        i = 1
        while i <= max:
            try:
                Post.objects.get(pk=self.pk + i)
                return reverse('blog:post', kwargs={'pk':self.pk+i})
                break
            except ObjectDoesNotExist:
                i += 1


    def get_last_url(self):
        max = Post.objects.latest('date').pk
        i = 1
        while i < max:
            try:
                Post.objects.get(pk=self.pk - i)
                return reverse('blog:post', kwargs={'pk': self.pk - i})
                break
            except ObjectDoesNotExist:
                i += 1

    def __str__(self):
        return self.title

