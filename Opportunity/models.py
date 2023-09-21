from django.db import models  

class Opportunity(models.Model):
	SequentialNo = models.CharField(max_length=9, blank=True) #56,
	CardCode = models.CharField(max_length=100, blank=True) #"C00002",
	SalesPerson = models.CharField(max_length=9, blank=True) #5,
	SalesPersonName = models.CharField(max_length=50, blank=True) #"Sunil Kumar",
	ContactPerson = models.CharField(max_length=9, blank=True) #6,
	ContactPersonName = models.CharField(max_length=50, blank=True) #"Manish Kumar",
	Source = models.CharField(max_length=100, blank=True) #null,  
	StartDate = models.CharField(max_length=50, blank=True) #"2021-09-10",
	PredictedClosingDate = models.CharField(max_length=50, blank=True) #"2021-09-15",
	MaxLocalTotal = models.CharField(max_length=100, blank=True) #100.0,
	MaxSystemTotal = models.CharField(max_length=100, blank=True) #1.515152, 
	Remarks = models.TextField(blank=True)
	Status = models.CharField(max_length=100, blank=True) #"sos_Open",
	ReasonForClosing = models.CharField(max_length=100, blank=True) #null,
	TotalAmountLocal = models.CharField(max_length=100, blank=True) #100.0,
	TotalAmounSystem = models.CharField(max_length=100, blank=True) #1.515152,
	CurrentStageNo = models.CharField(max_length=3, blank=True) #3,
	CurrentStageNumber = models.CharField(max_length=3, blank=True) #3,
	CurrentStageName = models.CharField(max_length=50, blank=True) #"Lead",
	OpportunityName = models.CharField(max_length=100, blank=True) #"Abs",
	Industry = models.CharField(max_length=100, blank=True) #null,
	LinkedDocumentType = models.CharField(max_length=100, blank=True) #null,
	DataOwnershipfield = models.IntegerField(default=0) #null,    
	DataOwnershipName = models.CharField(max_length=50, blank=True) #"Rakesh Kumar",
	StatusRemarks = models.TextField(blank=True)
	ProjectCode = models.CharField(max_length=100, blank=True) #null,
	CustomerName = models.CharField(max_length=100, blank=True) #"SBI Bank",
	ClosingDate = models.CharField(max_length=100, blank=True) #null,
	ClosingType = models.CharField(max_length=100, blank=True) #"sos_Days",
	OpportunityType = models.CharField(max_length=100, blank=True) #"boOpSales",
	UpdateDate = models.CharField(max_length=50, blank=True) #"2021-09-10",
	UpdateTime = models.CharField(max_length=50, blank=True) #"16:31:10",
	U_LEADID = models.IntegerField(default=0)
	U_LEADNM = models.CharField(max_length=150, blank=True)
	U_TYPE = models.CharField(max_length=100, blank=True) #New | Existing,
	U_LSOURCE = models.CharField(max_length=100, blank=True) #null,
	U_FAV = models.CharField(max_length=100, blank=True) #null,
	U_PROBLTY = models.CharField(max_length=100, blank=True) #null,
	DivCode = models.CharField(max_length=50, blank=True)
	DivName = models.CharField(max_length=50, blank=True)
	OppType = models.CharField(max_length=20, blank=True) #Tender|Normal
	BPStatus = models.CharField(max_length=2, blank=True)
	QTStatus = models.CharField(max_length=2, blank=True)
	TDStatus = models.CharField(max_length=2, blank=True)
	ODStatus = models.CharField(max_length=2, blank=True)
	OPStatus = models.CharField(max_length=100, blank=True)
	SolutionType = models.CharField(max_length=100, blank=True)    
	category = models.TextField(blank=True)
	intProdCat = models.TextField(blank=True)
	intProjCat = models.TextField(blank=True)
     
	INStatus = models.CharField(max_length=2, blank=True)
	PRStatus = models.CharField(max_length=2, blank=True)
	STStatus = models.CharField(max_length=2, blank=True)
	RFStatus = models.CharField(max_length=2, blank=True)
	DepName = models.CharField(max_length=150, blank=True)
	CreatedBy = models.CharField(max_length=50, blank=True)
    
	tender_status = models.CharField(max_length=10, blank=True) #updated by millan on 22-09-2022
	OppStatus = models.CharField(max_length=30, blank=True, default="")



#--------line 0 ----
class Line(models.Model):
	LineNum = models.CharField(max_length=9, blank=True) #0,
	SalesPerson = models.CharField(max_length=9, blank=True) #-1,
	StartDate = models.CharField(max_length=50, blank=True) #"2021-09-10",
	ClosingDate = models.CharField(max_length=50, blank=True) #"2021-09-14",
	StageKey = models.CharField(max_length=9, blank=True) #2,
	MaxLocalTotal = models.CharField(max_length=100, blank=True) #100.0,
	MaxSystemTotal = models.CharField(max_length=100, blank=True) #1.520,
	Remarks = models.TextField(blank=True)
	Contact = models.CharField(max_length=100, blank=True) #"tNO",------
	Status = models.CharField(max_length=100, blank=True) #"so_Closed",
	ContactPerson = models.CharField(max_length=100, blank=True) #null,
	SequenceNo = models.CharField(max_length=9, blank=True) #56,
	Opp_Id = models.IntegerField(default=0) #56,

class Stage(models.Model):
    SequenceNo = models.CharField(max_length=9, blank=True) #2,
    Name = models.CharField(max_length=100, blank=True) #Lead",
    Stageno = models.FloatField(default=0) #1,
    ClosingPercentage = models.CharField(max_length=100, blank=True) # 0.0,
    Cancelled = models.CharField(max_length=100, blank=True) #tNO",
    IsSales = models.CharField(max_length=100, blank=True) #tYES",
    IsPurchasing = models.CharField(max_length=100, blank=True) #tYES"
    Comment = models.TextField(blank=True)
    File = models.CharField(max_length=200, blank=True)
    CreateDate = models.CharField(max_length=60, blank=True)
    UpdateDate = models.CharField(max_length=60, blank=True)
    Status = models.IntegerField(default=0)
    Opp_Id = models.IntegerField(default=0) #tYES"

class StaticStage(models.Model):
    SequenceNo = models.CharField(max_length=9, blank=True) #2,
    Name = models.CharField(max_length=100, blank=True) #Lead",
    Stageno = models.FloatField(default='0') #1,
    ClosingPercentage = models.CharField(max_length=100, blank=True) # 0.0,
    Cancelled = models.CharField(max_length=100, blank=True) #tNO",
    IsSales = models.CharField(max_length=100, blank=True) #tYES",
    UTYPE = models.CharField(max_length=100, blank=True)
    IsPurchasing = models.CharField(max_length=100, blank=True) #tYES"


class OppItem(models.Model):
	LineNum = models.IntegerField(default=0)
	OppID = models.CharField(max_length=5, blank=True)
	Quantity = models.IntegerField(default=0)
	UnitPrice = models.FloatField(default=0)
	DiscountPercent = models.FloatField(default=0)
	ItemCode = models.CharField(max_length=20, blank=True)
	ItemDescription = models.CharField(max_length=150, blank=True)
	TaxCode = models.CharField(max_length=10, blank=True)
	U_FGITEM = models.CharField(max_length=20, blank=True)
	CostingCode2 = models.CharField(max_length=20, blank=True)
	ProjectCode = models.CharField(max_length=20, blank=True)
	FreeText = models.TextField(blank=True)
 	#added by millan on 03-November-2022
	Tax = models.FloatField(default=0)
	UomNo = models.CharField(max_length=100, blank=True)
 	#added by millan on 03-November-2022
	IT_MICharges = models.CharField(max_length=100, blank=True)
	IT_LOCharges = models.CharField(max_length=100, blank=True)
	IT_Intall = models.CharField(max_length=100, blank=True)

	# for service app
	Frequency = models.CharField(max_length=10, blank=True)
	StartDate = models.CharField(max_length=50, blank=True)
	EndDate = models.CharField(max_length=50, blank=True)
	ReferenceItem = models.CharField(max_length=255, blank=True)
	ReferenceSerial = models.CharField(max_length=255, blank=True)
	IsService 		= models.CharField(max_length=10, default="tNO")

############### CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT ################
class PreSite(models.Model):
    Stageno = models.FloatField(default=2)
    StartDate = models.CharField(max_length=100, blank=True)
    CompletedDate = models.CharField(max_length=100, blank=True)
    Shaft = models.CharField(max_length=250, blank=True)
    ShaftWidth = models.CharField(max_length=250, blank=True)
    ShaftDepth = models.CharField(max_length=250, blank=True)
    TotalTravel = models.CharField(max_length=250, blank=True)
    SideWallA = models.CharField(max_length=250, blank=True)
    SideWallC = models.CharField(max_length=250, blank=True)
    PitDepth = models.CharField(max_length=250, blank=True)    
    Comments = models.TextField(blank=True)
    Opp_Id = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    UpdateDate = models.CharField(max_length=60, blank=True)
    UpdateTime = models.CharField(max_length=60, blank=True)    

class Site(models.Model):
    Stageno = models.FloatField(default=2)
    StartDate = models.CharField(max_length=100, blank=True)
    CompletedDate = models.CharField(max_length=100, blank=True)
    Shaft = models.CharField(max_length=250, blank=True)
    ShaftWidth = models.CharField(max_length=250, blank=True)
    ShaftDepth = models.CharField(max_length=250, blank=True)
    TotalTravel = models.CharField(max_length=250, blank=True)
    SideWallA = models.CharField(max_length=250, blank=True)
    SideWallC = models.CharField(max_length=250, blank=True)
    PitDepth = models.CharField(max_length=250, blank=True)    
    Comments = models.TextField(blank=True)
    Opp_Id = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    UpdateDate = models.CharField(max_length=60, blank=True)
    UpdateTime = models.CharField(max_length=60, blank=True)    

class RFQ(models.Model):
    Stageno = models.FloatField(default=3)
    StartDate = models.CharField(max_length=100, blank=True)
    CompletedDate = models.CharField(max_length=100, blank=True)
    SupplierCost = models.FloatField(default=0)
    Comments = models.TextField(blank=True)
    Opp_Id = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    UpdateDate = models.CharField(max_length=60, blank=True)
    UpdateTime = models.CharField(max_length=60, blank=True)        
    
class Initiation(models.Model):
    Stageno = models.FloatField(default=1)
    StartDate = models.CharField(max_length=100, blank=True)
    CompletedDate = models.CharField(max_length=100, blank=True)
    Comments = models.TextField(blank=True)
    Opp_Id = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    UpdateDate = models.CharField(max_length=60, blank=True)
    UpdateTime = models.CharField(max_length=60, blank=True)
