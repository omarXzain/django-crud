from django.db import models
from django.urls import reverse

# Create your models here.
class Crud(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField()
    eater = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # eater = models.CharField(max_length=64, default="omar")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

