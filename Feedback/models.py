from django.db import models  

class Feedback(models.Model):
    Remark = models.TextField(max_length=2000, blank=True, unique=False)
    SourceType = models.CharField(max_length=50, blank=True, unique=False)
    Type = models.CharField(max_length=50, blank=True, unique=False, choices = [('1', 'Poor'), ('2', 'Average'), ('3', 'Good'), ('4', 'Excelent')], default="Good")
    Rating = models.CharField(max_length=50, blank=True, unique=False)
    SourceID = models.CharField(max_length=10, blank=True, unique=False)
    CardCode = models.CharField(max_length=20, blank=True, unique=False)
    CreatedDate = models.CharField(max_length=20, blank=True, unique=False)
    CreatedTime = models.CharField(max_length=20, blank=True, unique=False)

