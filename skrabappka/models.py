from django.db import models

# Create your models here.
class Scratching(models.Model):
    dateandtime = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    person = models.CharField(max_length=20, blank=False)
    minutes = models.IntegerField()

