from django.db import models  
from Category.models import *


######################################### # Added  for Item Master group ######################

class ItemGroupMaster(models.Model):
	Number = models.IntegerField(default=0, unique=True)
	GroupName = models.CharField(max_length=100)
	def __str__ (self):
		return self.GroupName

################################################################################################


class Item(models.Model):
	UnitPrice = models.FloatField(default=0)
	Currency = models.CharField(max_length=50, default="INR")
	DiscountPercent = models.FloatField(default=0)
	ItemCode = models.CharField(max_length=50, blank=True)
	ItemName = models.CharField(max_length=150, blank=True)
	TaxCode = models.CharField(max_length=50, blank=True)
	U_DIV = models.CharField(max_length=10, blank=True)
	IsService = models.CharField(max_length=10, default="tNo")
	InStock = models.IntegerField(default=0)
	ItemsGroupCode = models.ForeignKey(Category, to_field="Number", on_delete = models.CASCADE, related_name='category')
	ManageSerialNumbers = models.CharField(max_length=10, default='tNO') #tYES/tNO
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
	approval_status = models.CharField(max_length=200, blank=True, default="Pending")# 0 Pending, 1 Approved, 2 Rejected
	approved_by = models.CharField(max_length=200, blank=True)
	# UV_Germ = models.TextField(max_length=1000, blank=True)
	# Sales_Type  = models.TextField(max_length=1000, blank=True)
	######################## New Fields add [DK] Machine specification ################

	ItemsGroupMasterCode = models.ForeignKey(ItemGroupMaster, to_field="Number", on_delete = models.CASCADE, related_name='ItemsGroupMasterCode', null=True, blank=True, default=1)



class ItemOrderStatusRemarks(models.Model):
    item_id    = models.CharField(max_length=5, blank=True)
    SalesEmployeeCode= models.CharField(max_length=5, blank=True)
    Status          = models.CharField(max_length=50, blank=True)
    Remarks         = models.CharField(max_length=255, blank=True)
    Datetime        = models.DateTimeField(auto_now_add=True)
    
class Tax(models.Model):
	Rate = models.FloatField(default=0)
	Name = models.CharField(max_length=50)
	Code = models.CharField(max_length=50)


class Department(models.Model):
	FactorCode = models.CharField(max_length=50)
	FactorDescription = models.CharField(max_length=150)



