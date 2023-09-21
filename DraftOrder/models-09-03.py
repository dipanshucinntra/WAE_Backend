from django.db import models  
from Employee.models import Employee
class DraftOrder(models.Model):
    TaxDate = models.CharField(max_length=30, blank=True)
    DocDueDate = models.CharField(max_length=30, blank=True)
    ContactPersonCode = models.CharField(max_length=5, blank=True)
    ContactPersonCodeEnd = models.CharField(max_length=5, blank=True)
    DiscountPercent = models.FloatField(default=0)
    DocDate = models.CharField(max_length=30, blank=True)
    CardCode = models.CharField(max_length=30, blank=True)
    CardCodeEnd = models.CharField(max_length=30, blank=True)
    Comments = models.CharField(max_length=150, blank=True)
    SalesPersonCode = models.CharField(max_length=5, blank=True)

    #info of contact person by input
    ContactPersonName = models.CharField(max_length=250, blank=True)
    ContactNumber = models.CharField(max_length=250, blank=True)
    Designation = models.CharField(max_length=250, blank=True)
    Email = models.CharField(max_length=250, blank=True)
    Address = models.CharField(max_length=250, blank=True)
    
    DocumentStatus = models.CharField(max_length=50, blank=True)
    CancelStatus = models.CharField(max_length=50, blank=True)
    DocCurrency = models.CharField(max_length=50, blank=True)
    DocTotal = models.CharField(max_length=50, blank=True)
    NetTotal = models.CharField(max_length=50, blank=True)
    CardName = models.CharField(max_length=150, blank=True)
    CardNameEnd = models.CharField(max_length=150, blank=True)
    VatSum = models.CharField(max_length=50, blank=True)    
    CreationDate = models.CharField(max_length=50, blank=True)
    
    OrdNo = models.CharField(max_length=50, blank=True)
    PoNo = models.CharField(max_length=50, blank=True)
    DatePO = models.CharField(max_length=150, blank=True)
    Attach = models.CharField(max_length=250, blank=True)
    Project = models.CharField(max_length=50, blank=True)
    
    DocEntry = models.CharField(max_length=5, blank=True)
    PaymentGroupCode = models.CharField(max_length=5, blank=True)
    U_Term_Condition = models.TextField(blank=True)
    U_TermInterestRate = models.FloatField(default=0)
    U_TermPaymentTerm = models.CharField(max_length=100, blank=True)
    U_TermDueDate = models.CharField(max_length=100, blank=True)
    
    U_QUOTNM = models.CharField(max_length=100, blank=True)
    U_QUOTID = models.IntegerField(default=0)    
    
    U_LEADID = models.IntegerField(default=0)
    U_LEADNM = models.CharField(max_length=150, blank=True)
    
    U_OPPID = models.CharField(max_length=5, blank=True)
    U_OPPRNM = models.CharField(max_length=100, blank=True)
    
    BPLID = models.CharField(max_length=5, blank=True)
    DelStatus = models.CharField(max_length=50, blank=True)
    
    CreateDate = models.CharField(max_length=30, blank=True)
    CreateTime = models.CharField(max_length=30, blank=True)
    UpdateDate = models.CharField(max_length=30, blank=True)
    UpdateTime = models.CharField(max_length=30, blank=True)
    
    #added by millan on 07-10-2022
    GroupType = models.CharField(max_length=100, blank=True)
    POAmount = models.CharField(max_length=100, blank=True)
    ProjectLocation = models.CharField(max_length=100, blank=True)
    OPSNumber = models.CharField(max_length=100, blank=True)
    UrlNo = models.CharField(max_length=100, blank=True)
    OtherInstruction = models.CharField(max_length=100, blank=True)
    GSTNo = models.CharField(max_length=100, blank=True)
    #added by millan on 07-10-2022
    
    #added by millan on 11-10-2022
    MICharges = models.CharField(max_length=100, blank=True)
    LOCharges = models.CharField(max_length=100, blank=True)
    Intall = models.CharField(max_length=100, blank=True)
    CivWork = models.CharField(max_length=100, blank=True)
    SSStatus = models.CharField(max_length=100, blank=True)
    PlumStatus = models.CharField(max_length=100, blank=True)
    #added by millan on 11-10-2022

    IncidentalCharges = models.CharField(max_length=100, blank=True)
    CivilWorkCharges = models.CharField(max_length=100, blank=True)
    PlumbingCharges = models.CharField(max_length=100, blank=True)
    
    #added by millan on 04-11-2022
    technical_details = models.CharField(max_length=20, blank=True)
    approved_drawing = models.CharField(max_length=20, blank=True)
    addendum = models.CharField(max_length=20, blank=True)
    special_instructions = models.CharField(max_length=20, blank=True)
    #added by millan on 04-11-2022
    
    URN = models.CharField(max_length=20, blank=True)  #added by millan on 07-11-2022
    # new keys
    PlumbingStatusSide = models.CharField(max_length=100, blank=True)
    CivilWorkSide = models.CharField(max_length=100, blank=True)
    SiteSurveySide = models.CharField(max_length=100, blank=True)
    SiteSurveySerialNo = models.CharField(max_length=100, blank=True)
    CrainCharges = models.CharField(max_length=100, blank=True)
    LabourCharges = models.CharField(max_length=100, blank=True)
    ConsultingFee = models.CharField(max_length=100, blank=True)
    SolutionType = models.CharField(max_length=100, blank=True)    

class AddressExtension(models.Model):
    OrderID = models.CharField(max_length=5, blank=True)
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
    OrderID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    DiscountPercent = models.FloatField(default=0)
    ItemDescription = models.CharField(max_length=150, blank=True)
    ItemCode = models.CharField(max_length=20, blank=True)
    TaxCode = models.CharField(max_length=50, blank=True)
    U_FGITEM = models.CharField(max_length=20, blank=True)
    CostingCode2 = models.CharField(max_length=20, blank=True)
    ProjectCode = models.CharField(max_length=20, blank=True)
    FreeText = models.CharField(max_length=500, blank=True)
    
    #added by millan on 01-November-2022
    Tap_Qty = models.CharField(max_length=50, blank=True)
    Tap_Type    = models.CharField(max_length=50, blank=True)
    Ht_Capacity = models.CharField(max_length=50, blank=True)
    Ct_Capacity = models.CharField(max_length=50, blank=True)
    At_Capacity = models.CharField(max_length=50, blank=True)
    Pro_Capacity    = models.CharField(max_length=50, blank=True)
    Machine_Dimension   = models.CharField(max_length=100, blank=True)
    Machine_Colour  = models.CharField(max_length=100, blank=True)
    Type_of_Machine = models.CharField(max_length=100, blank=True)
    Machine_Body_Material   = models.CharField(max_length=500, blank=True)
    UV_Germ = models.CharField(max_length=500, blank=True)
    Sales_Type  = models.CharField(max_length=100, blank=True)
    Special_Remark  = models.CharField(max_length=500, blank=True)

    IT_MICharges = models.CharField(max_length=100, blank=True)
    IT_LOCharges = models.CharField(max_length=100, blank=True)
    IT_Intall = models.CharField(max_length=100, blank=True)
    
    Tax = models.FloatField(default=0)
    UomNo = models.CharField(max_length=100, blank=True)
    #added by millan on 01-November-2022
    
#added by millan on 06-09-2022
class AddendumRequest(models.Model):
    OrderID = models.CharField(max_length=5, blank=False)
    Date = models.CharField(max_length=50, blank=False)
    Time = models.CharField(max_length=50, blank=False)
    Attachments = models.CharField(max_length=255, blank=False)
    
#added by millan on 04-11-2022 for urn number
class CustCode(models.Model):
    cc_prefix = models.CharField(max_length=100, blank=True)
    counter = models.IntegerField(default=0)
    OrderId = models.IntegerField(default=0)
    CustCodeBp = models.CharField(max_length=100, blank=False)


class TapType(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    CreatedDate = models.CharField(max_length=30, blank=True)
    CreatedTime = models.CharField(max_length=30, blank=True)

class MachineType(models.Model):
    Name = models.CharField(max_length=250, blank=False)
    CreatedDate = models.CharField(max_length=30, blank=True)
    CreatedTime = models.CharField(max_length=30, blank=True)

class AddOnDocumentLines(models.Model):
    LineNum = models.IntegerField(default=0)
    OrderID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    ItemDescription = models.CharField(max_length=150, blank=True)
    ItemCode = models.CharField(max_length=20, blank=True)
    ParentItemCode = models.CharField(max_length=20, blank=True)
