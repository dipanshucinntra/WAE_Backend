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

	######################## New Fields add [DK] Machine specification ################
	Tap_Qty = models.TextField(max_length=1000, blank=True)
	Tap_Type    = models.TextField(max_length=1000, blank=True)
	Ht_Capacity = models.TextField(max_length=1000, blank=True)
	Ct_Capacity = models.TextField(max_length=1000, blank=True)
	At_Capacity = models.TextField(max_length=1000, blank=True)
	Pro_Capacity    = models.TextField(max_length=1000, blank=True)
	Machine_Dimension   = models.TextField(max_length=1000, blank=True)
	Machine_Colour  = models.TextField(max_length=1000, blank=True)
	Type_of_Machine = models.TextField(max_length=1000, blank=True)
	Machine_Body_Material   = models.TextField(max_length=1000, blank=True)	
	Special_Remark  = models.TextField(blank=True)
	# UV_Germ = models.TextField(max_length=1000, blank=True)
	# Sales_Type  = models.TextField(max_length=1000, blank=True)
	######################## New Fields add [DK] Machine specification ################

class Tax(models.Model):
	Rate = models.FloatField(default=0)
	Name = models.CharField(max_length=50)
	Code = models.CharField(max_length=50)


class Department(models.Model):
	FactorCode = models.CharField(max_length=50)
	FactorDescription = models.CharField(max_length=150)

