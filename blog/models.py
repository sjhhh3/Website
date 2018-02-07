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
            #return reverse('post', kwargs={'pk':self.pk+1})
            #return Post.objects.latest('date')
            #return Post.objects.latest('date').pk
        #except ObjectDoesNotExist:
        max = Post.objects.latest('date').pk
        i = 1
        while i <= max:
            try:
                Post.objects.get(pk=self.pk + i)
                return reverse('post', kwargs={'pk':self.pk+i})
                break
            except ObjectDoesNotExist:
                i += 1


    def get_last_url(self):
        max = Post.objects.latest('date').pk
        i = 1
        while i < max:
            try:
                Post.objects.get(pk=self.pk - i)
                return reverse('post', kwargs={'pk': self.pk - i})
                break
            except ObjectDoesNotExist:
                i += 1

    def __str__(self):
        return self.title

class Apost(models.Model):

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def get_self_url(self):
        return reverse('apost', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    address = models.CharField(max_length=60, default='Unknown')
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=140)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.author