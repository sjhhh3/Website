from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Create your models here.
class Notepost(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    #def get_next_url(self):
     #   return reverse('notepost', kwargs={'pk':self.pk+1})
    #def get_last_url(self):
    #    return reverse('notepost', kwargs={'pk':self.pk-1})

    def get_next_url(self):
        max = Notepost.objects.latest('date').pk
        i = 1
        while i <= max:
            try:
                Notepost.objects.get(pk=self.pk + i)
                return reverse('notepost', kwargs={'pk':self.pk+i})
                break
            except ObjectDoesNotExist:
                i += 1


    def get_last_url(self):
        max = Notepost.objects.latest('date').pk
        i = 1
        while i < max:
            try:
                Notepost.objects.get(pk=self.pk - i)
                return reverse('notepost', kwargs={'pk': self.pk - i})
                break
            except ObjectDoesNotExist:
                i += 1

    def __str__(self):
        return self.title