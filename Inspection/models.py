from django.db import models

class Inspection(models.Model):
    IssueType = models.CharField(max_length=100, blank=True, unique=False)
    Description = models.TextField(max_length=1000, blank=True, unique=False)
    TicketId = models.CharField(max_length=20, blank=True, unique=False)
    CreatedBy = models.CharField(max_length=20, blank=True, unique=False)
    CreatedDate = models.CharField(max_length=20, blank=True, unique=False)
    CreatedTime = models.CharField(max_length=20, blank=True, unique=False)

