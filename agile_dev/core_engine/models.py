from django.db import models


# Create your models here.
class ContextValues(models.Model):
    title = models.CharField(max_length=200)
    values_desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)


class ContextPrinciple(models.Model):
    title = models.CharField(max_length=200)
    principles_desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
