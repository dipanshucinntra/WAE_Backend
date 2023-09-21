from enum import auto
from django.db import models  
from Employee.models import Employee
class TenderQuotation(models.Model):
    TaxDate = models.CharField(max_length=30, blank=True)
    DocDueDate = models.CharField(max_length=30, blank=True)
    ContactPersonCode = models.CharField(max_length=5, blank=True)
    DiscountPercent = models.FloatField(max_length=5, blank=True)
    DocDate = models.CharField(max_length=30, blank=True)
    CardCode = models.CharField(max_length=30, blank=True)
    Comments = models.CharField(max_length=150, blank=True)
    SalesPersonCode = models.CharField(max_length=5, blank=True)
    
    DocumentStatus = models.CharField(max_length=50, blank=True)
    CancelStatus = models.CharField(max_length=50, blank=True)
    DocCurrency = models.CharField(max_length=50, blank=True)
    DocTotal = models.CharField(max_length=50, blank=True)
    CardName = models.CharField(max_length=150, blank=True)
    VatSum = models.CharField(max_length=50, blank=True)
    CreationDate = models.CharField(max_length=50, blank=True)
    
    DocEntry = models.CharField(max_length=5, blank=True)
    PaymentGroupCode = models.CharField(max_length=5, blank=True)
    U_QUOTNM = models.CharField(max_length=100, blank=True)
    U_PREQUOTATION = models.CharField(max_length=100, blank=True)
    U_PREQTNM = models.CharField(max_length=250, blank=True)
    
    U_LEADID = models.IntegerField(default=0)
    U_LEADNM = models.CharField(max_length=150, blank=True)
    
    U_Term_Condition = models.TextField(blank=True)
    U_TermInterestRate = models.FloatField(default=0)
    U_TermPaymentTerm = models.CharField(max_length=100, blank=True)
    U_TermDueDate = models.CharField(max_length=100, blank=True)
    
    BPLID = models.CharField(max_length=5, blank=True)
    
    U_OPPID = models.CharField(max_length=5, blank=True)
    U_TENDERID = models.CharField(max_length=50, blank=True)
    U_OPPRNM = models.CharField(max_length=100, blank=True)
    
    U_FAV = models.CharField(max_length=10, blank=True)
    APPROVEID = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="TQAPPROVEID", on_delete = models.CASCADE, blank=True, null=True)
    U_APPROVENM = models.CharField(max_length=30, blank=True)
    
    Level1 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="TQLevel1", on_delete = models.CASCADE, blank=True, null=True)
    Level1Status = models.CharField(max_length=30, blank=True)
    
    Level2 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="TQLevel2", on_delete = models.CASCADE, blank=True, null=True)    
    Level2Status = models.CharField(max_length=30, blank=True)
    
    Level3 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="TQLevel3", on_delete = models.CASCADE, blank=True, null=True)
    Level3Status = models.CharField(max_length=30, blank=True)
    
    FinalStatus = models.CharField(max_length=30, blank=True)
    
    CreateDate = models.CharField(max_length=30, blank=True)
    CreateTime = models.CharField(max_length=30, blank=True)
    UpdateDate = models.CharField(max_length=30, blank=True)
    UpdateTime = models.CharField(max_length=30, blank=True)
    
    PoNo                = models.CharField(max_length=30, blank=True)
    PoAmt               = models.CharField(max_length=30, blank=True)
    PoDate              = models.CharField(max_length=255, blank=True)
    PRID                = models.CharField(max_length=255, blank=True)
    
    ShippingAndHandling = models.CharField(max_length=10, blank=True)
    TermsAndConditions  = models.TextField(blank=True)

class AddressExtension(models.Model):
    TenderQuotationID = models.CharField(max_length=5, blank=True)
    BillToBuilding = models.CharField(max_length=100, blank=True)
    ShipToState = models.CharField(max_length=100, blank=True)
    BillToCity = models.CharField(max_length=100, blank=True)
    ShipToCountry = models.CharField(max_length=100, blank=True)
    BillToZipCode = models.CharField(max_length=100, blank=True)
    ShipToStreet = models.CharField(max_length=100, blank=True)
    BillToState = models.CharField(max_length=100, blank=True)
    ShipToZipCode = models.CharField(max_length=100, blank=True)
    BillToStreet = models.CharField(max_length=100, blank=True)
    ShipToBuilding = models.CharField(max_length=100, blank=True)
    ShipToCity = models.CharField(max_length=100, blank=True)
    BillToCountry = models.CharField(max_length=100, blank=True)
    
    U_SCOUNTRY = models.CharField(max_length=100, blank=True)
    U_SSTATE = models.CharField(max_length=100, blank=True)
    U_SHPTYPB = models.CharField(max_length=100, blank=True)
    U_BSTATE = models.CharField(max_length=100, blank=True)
    U_BCOUNTRY = models.CharField(max_length=100, blank=True)
    U_SHPTYPS = models.CharField(max_length=100, blank=True)

class DocumentLines(models.Model):
    LineNum = models.IntegerField(default=0)
    TenderQuotationID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    DiscountPercent = models.FloatField(default=0)
    ItemCode = models.CharField(max_length=20, blank=True)
    ItemDescription = models.CharField(max_length=150, blank=True)
    TaxCode = models.CharField(max_length=10, blank=True)
    TaxRate = models.CharField(max_length=10, blank=True,default=0)
    U_FGITEM = models.CharField(max_length=20, blank=True)
    CostingCode2 = models.CharField(max_length=20, blank=True)
    ProjectCode = models.CharField(max_length=20, blank=True)
    FreeText = models.CharField(max_length=500, blank=True)
    ItemType = models.CharField(max_length=500, blank=True, default='paid')
    # for service app
    Frequency = models.CharField(max_length=10, blank=True)
    StartDate = models.CharField(max_length=50, blank=True)
    EndDate = models.CharField(max_length=50, blank=True)
    ReferenceItem = models.CharField(max_length=255, blank=True)
