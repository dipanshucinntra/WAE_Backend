from django.db import models  
from Category.models import *
class Item(models.Model):
	UnitPrice = models.FloatField(default=0)
	Currency = models.CharField(max_length=50, default="INR")
	DiscountPercent = models.FloatField(default=0)
	ItemCode = models.CharField(max_length=50, blank=True)
	ItemName = models.CharField(max_length=150, blank=True)
	TaxCode = models.CharField(max_length=50, blank=True)
	U_DIV = models.CharField(max_length=10, blank=True)
	InStock = models.IntegerField(default=0)
	ItemsGroupCode = models.ForeignKey(Category, to_field="Number", on_delete = models.CASCADE)
 
	UomNo = models.CharField(max_length=100, blank=True)	#added by millan on 10-10-2022

class Tax(models.Model):
	Rate = models.FloatField(default=0)
	Name = models.CharField(max_length=50)
	Code = models.CharField(max_length=50)


class Department(models.Model):
	FactorCode = models.CharField(max_length=50)
	FactorDescription = models.CharField(max_length=150)

