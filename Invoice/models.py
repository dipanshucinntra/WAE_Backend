from django.db import models  

class Invoice(models.Model):
    TaxDate = models.CharField(max_length=30, blank=True)
    DocDueDate = models.CharField(max_length=30, blank=True)
    ContactPersonCode = models.CharField(max_length=5, blank=True)
    DiscountPercent = models.FloatField(default=0)
    DocDate = models.CharField(max_length=30, blank=True)
    CardCode = models.CharField(max_length=30, blank=True)
    Comments = models.CharField(max_length=150, blank=True)
    SalesPersonCode = models.CharField(max_length=5, blank=True)
    
    DocumentStatus = models.CharField(max_length=50, blank=True)
    DocCurrency = models.CharField(max_length=50, blank=True)
    DocTotal = models.CharField(max_length=50, blank=True)
    CardName = models.CharField(max_length=150, blank=True)
    VatSum = models.CharField(max_length=50, blank=True)
    CreationDate = models.CharField(max_length=50, blank=True)
    
    DocEntry = models.CharField(max_length=5, blank=True)
    PaymentGroupCode = models.CharField(max_length=5, blank=True)
    U_Term_Condition = models.TextField(blank=True)

    IncidentalCharges = models.CharField(max_length=100, blank=True)
    CivilWorkCharges = models.CharField(max_length=100, blank=True)
    PlumbingCharges = models.CharField(max_length=100, blank=True)

    
    BPLID = models.CharField(max_length=5, blank=True)
    
    CreateDate = models.CharField(max_length=30, blank=True)
    CreateTime = models.CharField(max_length=30, blank=True)
    UpdateDate = models.CharField(max_length=30, blank=True)
    UpdateTime = models.CharField(max_length=30, blank=True)

class AddressExtension(models.Model):
    InvoiceID = models.CharField(max_length=5, blank=True)
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
    InvoiceID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    DiscountPercent = models.FloatField(default=0)
    ItemDescription = models.CharField(max_length=150, blank=True)
    ItemCode = models.CharField(max_length=20, blank=True)
    TaxCode = models.CharField(max_length=10, blank=True)
    U_FGITEM = models.CharField(max_length=20, blank=True)
    CostingCode2 = models.CharField(max_length=20, blank=True)
    ProjectCode = models.CharField(max_length=20, blank=True)
    FreeText = models.CharField(max_length=500, blank=True)
    IT_MICharges = models.CharField(max_length=100, blank=True)
    IT_LOCharges = models.CharField(max_length=100, blank=True)
    IT_Intall = models.CharField(max_length=100, blank=True)

############### CODE ADDED BY DIPANSHU KUMAR FROM STANDALONE SUPPORT #################

class IncomingPaymentInvoices(models.Model):
    IncomingPaymentsId = models.CharField(max_length=10, blank=True)
    LineNum  = models.CharField(max_length=100, blank=True)
    InvoiceDocEntry = models.CharField(max_length=100, blank=True)
    SumApplied = models.CharField(max_length=100, blank=True)
    AppliedFC  = models.CharField(max_length=100, blank=True)
    AppliedSys  = models.CharField(max_length=100, blank=True)
    DiscountPercent = models.CharField(max_length=100, blank=True)
    TotalDiscount = models.CharField(max_length=100, blank=True)
    TotalDiscountFC = models.CharField(max_length=100, blank=True)
    TotalDiscountSC = models.CharField(max_length=100, blank=True)
    DocDate = models.CharField(max_length=100, blank=True)

class IncomingPayments(models.Model):   
    DocNum = models.CharField(max_length=100, blank=True)
    DocType = models.CharField(max_length=100, blank=True)
    DocDate = models.CharField(max_length=100, blank=True)
    CardCode = models.CharField(max_length=100, blank=True)
    CardName = models.CharField(max_length=100, blank=True)
    Address = models.CharField(max_length=100, blank=True)
    DocCurrency = models.CharField(max_length=100, blank=True)
    CheckAccount = models.CharField(max_length=100, blank=True)
    TransferAccount = models.CharField(max_length=100, blank=True)
    TransferSum = models.CharField(max_length=100, blank=True)
    TransferDate = models.CharField(max_length=100, blank=True)
    TransferReference = models.CharField(max_length=100, blank=True)
    Series = models.CharField(max_length=100, blank=True)
    DocEntry = models.CharField(max_length=100, blank=True)
    DueDate = models.CharField(max_length=100, blank=True)
    BPLID = models.CharField(max_length=100, blank=True)
    BPLName = models.CharField(max_length=100, blank=True)
    Comments = models.CharField(max_length=150, blank=True)

class CreditNotes(models.Model):
    InvoiceDocEntry = models.CharField(max_length=10, blank=True)
    DocEntry = models.CharField(max_length=10, blank=True)
    CardCode = models.CharField(max_length=50, blank=True)
    CardName = models.CharField(max_length=50, blank=True)
    DocDate = models.CharField(max_length=100, blank=True)
    DocTotal = models.CharField(max_length=100, blank=True)
    SalesPersonCode = models.CharField(max_length=100, blank=True)
    Comments = models.CharField(max_length=150, blank=True)



   