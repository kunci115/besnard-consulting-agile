from django.db import models


# Create your models here.
class ContextValues(models.Model):
    title = models.CharField(max_length=30)
    values_desc = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class ContextPrinciple(models.Model):
    title = models.CharField(max_length=30)
    principles_desc = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
