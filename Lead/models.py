from django.db import models  
from Employee.models import *
class Lead(models.Model):
    date = models.CharField(max_length=60, blank=True)
    code = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=100, blank=True)
    companyName = models.CharField(max_length=100, blank=True)
    numOfEmployee = models.IntegerField(default='0')
    turnover = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    source_id = models.CharField(max_length=10, blank=True)
    contactPerson = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    message = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    leadType = models.CharField(max_length=50, blank=True)
    productInterest = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    assignedTo = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignedTo')
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #employeeId = models.IntegerField(default='0')
    tender = models.IntegerField(default='0')

    category = models.CharField(max_length=250, blank=True)
    groupType = models.CharField(max_length=250, blank=True)
    intProdCat = models.CharField(max_length=250, blank=True)
    intProjCat = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    country_code = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    state_code = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)

    DivCode = models.CharField(max_length=50, blank=True)
    DivName = models.CharField(max_length=50, blank=True)
    BPStatus = models.CharField(max_length=2, blank=True)
    OPStatus = models.CharField(max_length=2, blank=True)
    TDStatus = models.CharField(max_length=2, blank=True)
    QTStatus = models.CharField(max_length=2, blank=True)
    ODStatus = models.CharField(max_length=2, blank=True)
    junk = models.IntegerField(default='0')
    timestamp = models.CharField(max_length=60, blank=True)

class Chatter(models.Model):
    Message = models.CharField(max_length=250, blank=True)
    Lead_Id = models.CharField(max_length=10, blank=True)
    Emp_Id = models.CharField(max_length=10, blank=True)
    Emp_Name = models.CharField(max_length=50, blank=True)
    UpdateDate = models.CharField(max_length=100, blank=True)
    UpdateTime = models.CharField(max_length=100, blank=True)

class Type(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    CreatedDate = models.CharField(max_length=50, blank=True)
    CreatedTime = models.CharField(max_length=50, blank=True)

class LeadItem(models.Model):
	LineNum = models.IntegerField(default=0)
	LeadID = models.CharField(max_length=5, blank=True)
	Quantity = models.IntegerField(default=0)
	UnitPrice = models.FloatField(default=0)
	DiscountPercent = models.FloatField(default=0)
	ItemCode = models.CharField(max_length=20, blank=True)
	ItemDescription = models.CharField(max_length=150, blank=True)
	TaxCode = models.CharField(max_length=10, blank=True)
	U_FGITEM = models.CharField(max_length=20, blank=True)
	CostingCode2 = models.CharField(max_length=20, blank=True)
	ProjectCode = models.CharField(max_length=20, blank=True)
	FreeText = models.CharField(max_length=500, blank=True)

class Source(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    CreatedDate = models.CharField(max_length=50, blank=True)
    CreatedTime = models.CharField(max_length=50, blank=True)
