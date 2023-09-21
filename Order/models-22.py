from django.db import models  
from Employee.models import Employee
class Order(models.Model):
    TaxDate = models.CharField(max_length=30, blank=True)
    DocDueDate = models.CharField(max_length=30, blank=True)
    ContactPersonCode = models.CharField(max_length=5, blank=True)
    ContactPersonCodeEnd = models.CharField(max_length=5, blank=True)
    DiscountPercent = models.FloatField(default=0)
    DocDate = models.CharField(max_length=30, blank=True)
    CardCode = models.CharField(max_length=30, blank=True)
    CardCodeEnd = models.CharField(max_length=30, blank=True)
    Comments = models.TextField(blank=True)
    SalesPersonCode = models.CharField(max_length=5, blank=True)

    #info of contact person by input
    ContactPersonName = models.CharField(max_length=250, blank=True)
    ContactNumber = models.CharField(max_length=250, blank=True)
    Designation = models.CharField(max_length=250, blank=True)
    Email = models.CharField(max_length=250, blank=True)
    Address = models.TextField(blank=True)
    
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
    PoNo = models.TextField(blank=True)
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

    # for approval process
    OrdLevel1 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="OrdLevel1", on_delete = models.CASCADE, blank=True, null=True)
    OrdLevel1Status = models.CharField(max_length=30, blank=True)
    
    OrdLevel2 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="OrdLevel2", on_delete = models.CASCADE, blank=True, null=True)    
    OrdLevel2Status = models.CharField(max_length=30, blank=True)
    
    OrdLevel3 = models.ForeignKey(Employee, to_field="SalesEmployeeCode", related_name="OrdLevel3", on_delete = models.CASCADE, blank=True, null=True)
    OrdLevel3Status = models.CharField(max_length=30, blank=True)
    
    FinalStatus = models.CharField(max_length=30, blank=True)
    
    ReadLevel1 = models.CharField(max_length=5, blank=True)
    ReadLevel2 = models.CharField(max_length=5, blank=True)
    ReadLevel3 = models.CharField(max_length=5, blank=True)
    
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
    OtherInstruction = models.TextField(blank=True)
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
    technical_details = models.TextField(blank=True)
    approved_drawing = models.CharField(max_length=20, blank=True)
    addendum = models.CharField(max_length=20, blank=True)
    special_instructions = models.TextField(blank=True)
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
    
    #these keys are for project

    kit_consultant_code = models.CharField(max_length=250, blank=True)
    kit_consultant_name = models.CharField(max_length=250, blank=True)
    kit_contact_person = models.CharField(max_length=250, blank=True)

    mep_consultant_code = models.CharField(max_length=250, blank=True)
    mep_consultant_name = models.CharField(max_length=250, blank=True)
    mep_contact_person = models.CharField(max_length=250, blank=True)
    
    pm_consultant_code = models.CharField(max_length=250, blank=True)
    pm_consultant_name = models.CharField(max_length=250, blank=True)
    pm_contact_person = models.CharField(max_length=250, blank=True)
    
    cli_consultant_code = models.CharField(max_length=250, blank=True)
    cli_consultant_name = models.CharField(max_length=250, blank=True)
    cli_contact_person = models.CharField(max_length=250, blank=True)
    
    contr_consultant_code = models.CharField(max_length=250, blank=True)
    contr_consultant_name = models.CharField(max_length=250, blank=True)
    contr_contact_person = models.CharField(max_length=250, blank=True)
    
    fcm_consultant_code = models.CharField(max_length=250, blank=True)
    fcm_consultant_name = models.CharField(max_length=250, blank=True)
    fcm_contact_person = models.CharField(max_length=250, blank=True)
    
    arch_consultant_code = models.CharField(max_length=250, blank=True)
    arch_consultant_name = models.CharField(max_length=250, blank=True)
    arch_contact_person = models.CharField(max_length=250, blank=True)
    
    oth_consultant_code = models.CharField(max_length=250, blank=True)
    oth_consultant_name = models.CharField(max_length=250, blank=True)
    oth_contact_person = models.CharField(max_length=250, blank=True)
    
    #new added
    amendment_status = models.CharField(max_length=200, blank=True, default="Inactive")
    amendment_action = models.CharField(max_length=200, blank=True, default="0")




class AddressExtension(models.Model):
    OrderID = models.CharField(max_length=5, blank=True)
    BillToBuilding = models.TextField(blank=True)
    ShipToState = models.CharField(max_length=100, blank=True)
    BillToCity = models.CharField(max_length=100, blank=True)
    ShipToCountry = models.CharField(max_length=100, blank=True)
    BillToZipCode = models.CharField(max_length=100, blank=True)
    ShipToStreet = models.TextField(blank=True)
    BillToState = models.CharField(max_length=100, blank=True)
    ShipToZipCode = models.CharField(max_length=100, blank=True)
    BillToStreet = models.TextField(blank=True)
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
    ItemDescription = models.TextField(max_length=1000, blank=True)
    ItemCode = models.TextField(max_length=1000, blank=True)
    TaxCode = models.TextField(max_length=1000, blank=True)
    U_FGITEM = models.TextField(max_length=1000, blank=True)
    CostingCode2 = models.TextField(max_length=1000, blank=True)
    ProjectCode = models.TextField(max_length=1000, blank=True)
    FreeText = models.TextField(max_length=1000, blank=True)
    
    #added by millan on 01-November-2022
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
    UV_Germ = models.TextField(max_length=1000, blank=True)
    Sales_Type  = models.TextField(max_length=1000, blank=True)
    Special_Remark  = models.TextField(blank=True)

    IT_MICharges = models.TextField(max_length=1000, blank=True)
    IT_LOCharges = models.TextField(max_length=1000, blank=True)
    IT_Intall = models.TextField(max_length=1000, blank=True)
    
    Tax = models.FloatField(default=0)
    UomNo = models.TextField(max_length=1000, blank=True)
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

class AppSlave(models.Model):
    Min = models.FloatField(default=0)
    Max = models.FloatField(default=0)
    Level = models.IntegerField(default=0)

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
    ItemDescription = models.TextField(blank=True)
    ItemCode = models.CharField(max_length=20, blank=True)
    ParentItemCode = models.CharField(max_length=20, blank=True)



################################################## HISTORY ORDER AMENDMENT ############################################

class OrderHistory(models.Model):
    Number = models.IntegerField(default=0, blank=True)
    OrderID = models.CharField(max_length=200, blank=True)
    DocTotal = models.CharField(max_length=50, blank=True)
    NetTotal = models.CharField(max_length=50, blank=True)
    CreatedDate = models.CharField(max_length=30, blank=True)
    CreatedTime = models.CharField(max_length=30, blank=True)

class DocumentLinesHistory(models.Model):
    orderhistory_id = models.ForeignKey(OrderHistory, on_delete=models.CASCADE, null=True, blank=True)
    LineNum = models.IntegerField(default=0)
    OrderID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    DiscountPercent = models.FloatField(default=0)
    ItemDescription = models.TextField(max_length=1000, blank=True)
    ItemCode = models.TextField(max_length=1000, blank=True)
    TaxCode = models.TextField(max_length=1000, blank=True)
    U_FGITEM = models.TextField(max_length=1000, blank=True)
    CostingCode2 = models.TextField(max_length=1000, blank=True)
    ProjectCode = models.TextField(max_length=1000, blank=True)
    FreeText = models.TextField(max_length=1000, blank=True)
    
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
    UV_Germ = models.TextField(max_length=1000, blank=True)
    Sales_Type  = models.TextField(max_length=1000, blank=True)
    Special_Remark  = models.TextField(blank=True)

    IT_MICharges = models.TextField(max_length=1000, blank=True)
    IT_LOCharges = models.TextField(max_length=1000, blank=True)
    IT_Intall = models.TextField(max_length=1000, blank=True)
    
    Tax = models.FloatField(default=0)
    UomNo = models.TextField(max_length=1000, blank=True)
    

class AddOnDocumentLinesHistory(models.Model):
    documentlineshistory_id = models.ForeignKey(DocumentLinesHistory, on_delete=models.CASCADE, null=True, blank=True)
    LineNum = models.IntegerField(default=0)
    OrderID = models.CharField(max_length=5, blank=True)
    Quantity = models.IntegerField(default=0)
    UnitPrice = models.FloatField(default=0)
    ItemDescription = models.TextField(blank=True)
    ItemCode = models.CharField(max_length=20, blank=True)
    ParentItemCode = models.CharField(max_length=20, blank=True)



