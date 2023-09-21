from django.db import models

class Form(models.Model):
    Title = models.TextField(max_length=500, blank=False, unique=False)
    CreatedBy = models.CharField(max_length=50, blank=False, unique=False)
    CreatedDate = models.CharField(max_length=50, blank=False, unique=False)
    CreatedTime = models.CharField(max_length=50, blank=False, unique=False)
    Data = models.TextField(max_length=10000, blank=False, unique=False)
