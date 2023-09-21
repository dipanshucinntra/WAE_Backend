from django.db import models

class IssueCategory(models.Model):
    Title = models.CharField(max_length=250, blank=False, unique=False)
    CreatedBy = models.CharField(max_length=150, blank=True, unique=False)
    CreatedDate = models.CharField(max_length=50, blank=True, unique=False)
    CreatedTime = models.CharField(max_length=50, blank=True, unique=False)
