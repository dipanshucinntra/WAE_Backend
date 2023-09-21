from django.db import models

from Inspection.IssueCategory.models import IssueCategory

# Create your models here.

class Issue(models.Model):
    Title = models.CharField(max_length=250, blank=True, unique=False)
    IssueCategory = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    CreatedBy = models.CharField(max_length=150, blank=True, unique=False)
    CreatedDate = models.CharField(max_length=50, blank=True, unique=False)
    CreatedTime = models.CharField(max_length=50, blank=True, unique=False)
