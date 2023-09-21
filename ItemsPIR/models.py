from email.policy import default
from django.db import models

from Category.models import Category

# Create your models here.
# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> CheckList >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>
class CheckList(models.Model):
    CategoryId      = models.CharField(max_length=200, blank=True)
    Type            = models.CharField(max_length=100, blank=True) # Installation, Maintenance, Complaints 
    ListFor         = models.IntegerField(default = 1) # Customer(0), Engineer(1)
    LineNo          = models.IntegerField(default = 0)
    Name            = models.CharField(max_length=200, blank=True)