from email.policy import default
from django.db import models
from BusinessPartner.models import BusinessPartner
# from Delivery.models import Delivery
from Employee.models import Employee
from pytz import timezone

from datetime import date, datetime

now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> Tickets >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>
class Tickets(models.Model):
    DeliveryID          = models.CharField(max_length=100, blank=True)
    Stageno             = models.CharField(max_length=10, blank=True)
    AssignTo            = models.CharField(max_length=10, blank=True)
    CreatedBy           = models.CharField(max_length=10, blank=True)
    # Ticket header
    Type                = models.CharField(max_length=100, blank=True) # Installation, Maintenance, Complaints 
    TypeChange          = models.CharField(max_length=100, default="NO") # YES|NO
    SubType             = models.CharField(max_length=100, blank=True) # Installation, Maintenance, Complaints 
    Title               = models.CharField(max_length=250, blank=True)
    # contact person details
    BpCardCode          = models.CharField(max_length=100, blank=True) # Customer or Bp id
    BpBranch            = models.CharField(max_length=100, blank=True) # Customer or Bp branch id
    ContactName         = models.CharField(max_length=250, blank=True)
    ContactPhone        = models.CharField(max_length=100, blank=True)
    CountryCode        = models.CharField(max_length=100, blank=True)
    AlternatePhone      = models.CharField(max_length=100, blank=True)
    CountryCode1      = models.CharField(max_length=100, blank=True)
    ContactEmail        = models.CharField(max_length=250, blank=True)
    ContactAddress      = models.TextField(blank=True)
    # equpments details
    ProductSerialNo     = models.CharField(max_length=250, blank=True) #product serial no
    ProductName         = models.CharField(max_length=250, blank=True)
    ProductCategory     = models.CharField(max_length=250, blank=True)
    ProductModelNo      = models.CharField(max_length=250, blank=True)
    # ticket details
    Zone                = models.CharField(max_length=100, blank=True) # East, West, North, South
    Priority            = models.CharField(max_length=100, blank=True) # Standerd, Medium, Heigh 
    Status              = models.CharField(max_length=100, blank=True) # Pending, In progress, Assigned, Resolve
    Description         = models.TextField(blank=True)
    #Other Details
    DurationOfService   = models.CharField(max_length=100, blank=True, default="0:0")
    SignatureStatus     = models.CharField(max_length=100, blank=True, default="Pending") # Ticket Completion Confirmation Confirm
    # amc, cmc or warrenty
    WarrantyStartDate    = models.CharField(max_length=50, blank=True, default="")
    WarrantyDueDate      = models.CharField(max_length=50, blank=True, default="")
    ExtWarrantyStartDate = models.CharField(max_length=50, blank=True, default="")
    ExtWarrantyDueDate   = models.CharField(max_length=50, blank=True, default="")
    AMCStartDate         = models.CharField(max_length=50, blank=True, default="")
    AMCDueDate           = models.CharField(max_length=50, blank=True, default="")
    CMCStartDate         = models.CharField(max_length=50, blank=True, default="")
    CMCDueDate           = models.CharField(max_length=50, blank=True, default="")
    ContractType         = models.CharField(max_length=50, blank=True, default="")
    ManufacturingDate    = models.CharField(max_length=50, blank=True, default="")
    ExpiryDate           = models.CharField(max_length=50, blank=True, default="")
    #dates  
    CreateDate          = models.DateField(auto_now_add=True)
    ClosedDate          = models.CharField(max_length=50, blank=True)
    DueDate             = models.CharField(max_length=50, blank=True, default ="")
    Datetime            = models.DateTimeField(auto_now_add=True)
    #Datetime            = models.DateTimeField(default=datetime.now(timezone("Asia/Kolkata")), blank=True)
    #Datetime            = models.DateTimeField(default=now, blank=True)
    UpdatedDatetime     = models.DateTimeField(auto_now_add=True)
    TicketStatus        = models.CharField(max_length=50, blank=True, default ="Pending") # Accepted, Rejected
    PartRequest         = models.IntegerField(default =0) # 0 No 1 Yes
    # Ticket Start and end date time
    TicketStartDate     = models.CharField(max_length=50, blank=True, default = "")
    TicketEndDate       = models.CharField(max_length=50, blank=True, default = "")

    SysScheduleDate     = models.CharField(max_length=50, blank=True)
    AppScheduleDate      = models.CharField(max_length=50, blank=True)
    # PIR
    Data                = models.TextField(blank=True, default = "")
    CustomerPIR         = models.CharField(max_length=250, blank=True, default = "")
    SignatureFile       = models.CharField(max_length=250, blank=True, default = "")
    CustomerFeedback    = models.CharField(max_length=250, blank=True, default = "")

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> History >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>
class History(models.Model):
    TicketId            = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
    PrevType            = models.CharField(max_length=100, blank=True) # Call, Service, Status Update
    Type                = models.CharField(max_length=100, blank=True) # Call, Service, Status Update
    Remarks             = models.CharField(max_length=100, blank=True)
    Datetime            = models.DateTimeField(auto_now_add=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> Rescue History >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>
class RescueHistory(models.Model):
    TicketId            = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
    Status              = models.CharField(max_length=100, blank=True) # On the way, Reached, Work in Progress, Rescue
    Remarks             = models.CharField(max_length=250, blank=True)
    Datetime            = models.DateTimeField(auto_now_add=True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> Conversation >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Conversation(models.Model):
    TicketId        = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
    OwnerId         = models.CharField(max_length=10, blank=True)
    OwnerType       = models.CharField(max_length=100, blank=True) # Employee or Customer
    Message         = models.CharField(max_length=255, blank=True)
    Type            = models.CharField(max_length=100, blank=True) # Private/Public
    Datetime        = models.DateTimeField(auto_now_add=True)

# >>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> Parts >>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>
# class Parts(models.Model):
#     TicketId        = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
#     OwnerId         = models.CharField(max_length=10, blank=True) # Employee or Customer
#     OwnerType       = models.CharField(max_length=20, blank=True, default="Employee") # Employee or Customer
#     ItemCode        = models.CharField(max_length=100, blank=True)
#     ItemQty         = models.CharField(max_length=100, blank=True)
#     Comments        = models.CharField(max_length=100, blank=True)
#     Status          = models.CharField(max_length=100, blank=True, default="Pending") # Delivered/Partially Delivered/Pending/Rejcted
#     BillToAddress   = models.CharField(max_length=100, blank=True)
#     Discount        = models.CharField(max_length=100, blank=True)
#     EstimateAmt     = models.CharField(max_length=100, blank=True)
#     Datetime        = models.DateTimeField(auto_now_add=True)

class PartRequest(models.Model):
    TicketId        = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
    OwnerId         = models.CharField(max_length=10, blank=True) # Employee or Customer
    OwnerType       = models.CharField(max_length=20, blank=True, default="Employee") # Employee or Customer
    BillToAddress   = models.CharField(max_length=255, blank=True)
    EstimateAmt     = models.CharField(max_length=100, blank=True)
    WarrantyStatus  = models.CharField(max_length=100, blank=True, default="Warranty Expired")
    WarrantyDate    = models.CharField(max_length=100, blank=True, default="")
    ApproverId      = models.CharField(max_length=10, blank=True) # Employee
    RequestedDate   = models.CharField(max_length=20, blank=True)
    ApprovedDate    = models.CharField(max_length=20, blank=True)
    Status          = models.CharField(max_length=100, blank=True, default="Pending") # Delivered/Partially Delivered/Pending/Rejcted
    Datetime        = models.DateTimeField(auto_now_add=True)

class PRItems(models.Model):
    PRID            = models.ForeignKey(PartRequest, on_delete=models.CASCADE, blank=True, default="")
    ItemCode        = models.CharField(max_length=100, blank=True)
    ItemQty         = models.CharField(max_length=100, blank=True)
    UnitPrice       = models.CharField(max_length=100, blank=True)
    Discount        = models.CharField(max_length=100, blank=True)
    Comments        = models.CharField(max_length=100, blank=True)
    Status          = models.CharField(max_length=100, blank=True, default="Pending") # Pending, Approve and Rejcted
    ProjectCode     = models.CharField(max_length=100, blank=True) # ItemGroupCode
    Datetime        = models.DateTimeField(auto_now_add=True)

class PRAttachments(models.Model):
    PRID            = models.ForeignKey(PartRequest, on_delete=models.CASCADE, blank=True, default="")
    Attachment      = models.CharField(max_length=100, blank=True)
    Datetime        = models.DateTimeField(auto_now_add=True)

class PRStatusRemarks(models.Model):
    PRID              = models.ForeignKey(PartRequest, on_delete=models.CASCADE, blank=True, default="")
    SalesEmployeeCode = models.CharField(max_length=10, blank=True)
    Status            = models.CharField(max_length=50, blank=True)
    Remarks           = models.CharField(max_length=255, blank=True)
    Datetime          = models.DateTimeField(auto_now_add=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> ServiceCheckList >>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ServiceCheckList(models.Model):
    TicketId        = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=True, default="")
    TaskName        = models.CharField(max_length=255, blank=True)
    Comment         = models.CharField(max_length=100, blank=True)
    Status          = models.CharField(max_length=100, default='False')
    Duration        = models.CharField(max_length=100, blank=True)
    Datetime        = models.DateTimeField(auto_now_add=True)

# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DropDown for type
class Type(models.Model):
    Type        = models.CharField(max_length=100, blank=True) #installation, Maintenance,
    Stageno        = models.CharField(max_length=2, blank=True) #installation, Maintenance,

# DropDown for subtype
class SubType(models.Model):
    Type        = models.CharField(max_length=100, blank=True) #installation, Maintenance,
    SubType     = models.CharField(max_length=100, blank=True) #installation, Maintenance,
    Stageno     = models.CharField(max_length=2, blank=True) #installation, Maintenance,
	
# DropDown for status
class Status(models.Model):
    Status      = models.CharField(max_length=25, blank=True) #New, Assigned, In-Progress, Pending, Resolved

# DropDown for TicketStatus
class TicketStatus(models.Model):
    TicketStatus= models.CharField(max_length=25, blank=True) #Pending, Accepted, Rejected

# DropDown for Priority
class Priority(models.Model):
    Priority    = models.CharField(max_length=25, blank=True) #Low, Medium, High

# DropDown for Zone
class Zone(models.Model):
    Zone        = models.CharField(max_length=25, blank=True) #Low, Medium, High
    
# TicketChecklist
class TicketChecklist(models.Model):
    Name = models.CharField(max_length=250, blank=True)
    Description = models.TextField(blank=True)
    Comment = models.TextField(blank=True)
    Data = models.TextField(blank=True)
    Field1 = models.CharField(max_length=250, blank=True)
    Field2 = models.CharField(max_length=250, blank=True)
    Field3 = models.CharField(max_length=250, blank=True)
    Field4 = models.CharField(max_length=250, blank=True)
    Field5 = models.CharField(max_length=250, blank=True)
    Status = models.IntegerField(default=0, blank=True)
    Duration = models.CharField(max_length=100, blank=True)
    TicketId = models.CharField(max_length=100, blank=True)
    CreatedDate = models.CharField(max_length=100, blank=True)
    CreatedTime = models.CharField(max_length=100, blank=True)
    UpdatedDate = models.CharField(max_length=100, blank=True)
    UpdatedTime = models.CharField(max_length=100, blank=True)

class Sos(models.Model):
    Type = models.CharField(max_length=100, blank=True)
    SourceType = models.CharField(max_length=100, blank=True)
    SourceID = models.CharField(max_length=5, blank=True)
    Read = models.CharField(max_length=5, blank=True)
    SalesEmployeeCode = models.CharField(max_length=5, blank=True)
    CreatedDateTime = models.DateTimeField(default=date.today)
