from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Create your models here.
class Photo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=140)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def get_self_url(self):
        return reverse('photo', kwargs={'pk':self.pk})

    def get_next_url(self):
        max = Photo.objects.latest('date').pk
        i = 1
        while i <= max:
            try:
                Photo.objects.get(pk=self.pk + i)
                return reverse('photo', kwargs={'pk':self.pk+i})
                break
            except ObjectDoesNotExist:
                i += 1


    def get_last_url(self):
        max = Photo.objects.latest('date').pk
        i = 1
        while i < max:
            try:
                Photo.objects.get(pk=self.pk - i)
                return reverse('photo', kwargs={'pk': self.pk - i})
                break
            except ObjectDoesNotExist:
                i += 1

    def __str__(self):
        return self.body

class PhotoComment(models.Model):
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)
    address = models.CharField(max_length=60, default='Unknown')
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=140)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.author