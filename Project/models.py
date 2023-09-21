from django.db import models  

class MasterProject(models.Model):
    name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=250, blank=True)
    start_date = models.CharField(max_length=50, blank=True)
    target_date = models.CharField(max_length=50, blank=True)
    details = models.CharField(max_length=1000, blank=True)
    CardCode = models.CharField(max_length=100, blank=True)    
    location = models.CharField(max_length=250, blank=True)
    project_owner = models.CharField(max_length=250, blank=True)
    project_cost = models.CharField(max_length=250, blank=True)
    project_status = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)
    order_id = models.CharField(max_length=100, blank=True)
    CreatedDate = models.CharField(max_length=50, blank=True)
    CreatedTime = models.CharField(max_length=50, blank=True)
    UpdateDate = models.CharField(max_length=50, blank=True)
    UpdateTime = models.CharField(max_length=50, blank=True)
    DepName = models.CharField(max_length=100, blank=True)
    CreatedBy = models.CharField(max_length=50, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=250)
    CurrentStageNo = models.FloatField(default=1, blank=False) #3,
    kit_consultant_code = models.CharField(max_length=250, blank=True)
    kit_consultant_name = models.CharField(max_length=250, blank=True)
    kit_contact_person = models.CharField(max_length=250, blank=True)

    mep_consultant_code = models.CharField(max_length=250, blank=True)
    mep_consultant_name = models.CharField(max_length=250, blank=True)
    mep_contact_person = models.CharField(max_length=250, blank=True)
    
    pm_consultant_code = models.CharField(max_length=250, blank=True)
    pm_consultant_name = models.CharField(max_length=250, blank=True)
    pm_contact_person = models.CharField(max_length=250, blank=True)
    
    customer_group_type = models.CharField(max_length=250, blank=True)
    contact_person = models.CharField(max_length=250, blank=True)
    
    start_date = models.CharField(max_length=50, blank=True)
    target_date = models.CharField(max_length=50, blank=True)
    completion_date = models.CharField(max_length=50, blank=True)    
    details = models.CharField(max_length=1000, blank=True)
    
    #cardcode = models.CharField(max_length=100, blank=True)    
    CardCode = models.CharField(max_length=100, blank=True)    
    sector = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=250, blank=True)
    project_owner = models.CharField(max_length=250, blank=True)
    project_cost = models.CharField(max_length=250, blank=True)
    project_status = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)

    master_id = models.CharField(max_length=100, blank=True)
    ItemCode = models.CharField(max_length=50, blank=True)
    CreatedDate = models.CharField(max_length=50, blank=True)
    CreatedTime = models.CharField(max_length=50, blank=True)
    CreatedBy = models.CharField(max_length=50, blank=True)

    DepName = models.CharField(max_length=100, blank=True)
    GroupType = models.CharField(max_length=100, blank=True) #added by millan on 10 October 2022
    
    #added by millan on 11-10-2022
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
    #added by millan on 11-10-2022


class ProjectStaticstage(models.Model):
    Name = models.CharField(max_length=150, blank=False)
    Stageno = models.FloatField(default=0, blank=False)
    PaymentPercentage = models.FloatField(default=0, blank=False)
    DepName = models.CharField(max_length=150, blank=True, default="New Product")

class ProjectStage(models.Model):
    ProjectId = models.CharField(max_length=50, blank=True)
    Name = models.CharField(max_length=150, blank=False)
    Stageno = models.FloatField(default=0, blank=False)
    PaymentPercentage = models.FloatField(default=0, blank=False)
    Status = models.IntegerField(default=0, blank=False)
    StageOwner = models.CharField(max_length=5, blank=True)
    StageAssign = models.CharField(max_length=5, blank=True)
    Comment = models.CharField(max_length=500, blank=True)
    Data = models.TextField(blank=True)
    File = models.CharField(max_length=250, blank=True)
    DepName = models.CharField(max_length=250, blank=True)
    CreateDate = models.CharField(max_length=100, blank=True)
    CreateTime = models.CharField(max_length=100, blank=True)
    UpdateDate = models.CharField(max_length=100, blank=True)
    UpdateTime = models.CharField(max_length=100, blank=True)

class ProjectItem(models.Model):
    LineNum         = models.IntegerField(default=0)
    ProjectId         = models.CharField(max_length=20, blank=True)
    Quantity        = models.IntegerField(default=0)
    UnitPrice       = models.FloatField(default=0)
    DiscountPercent = models.FloatField(default=0)
    ItemDescription = models.CharField(max_length=250, blank=True)
    CategoryName = models.CharField(max_length=250, blank=True)
    ItemCode        = models.CharField(max_length=50, blank=True)
    TaxRate         = models.CharField(max_length=10, blank=True, default=0)
    TaxCode         = models.CharField(max_length=50, blank=True)
    U_FGITEM        = models.CharField(max_length=50, blank=True)
    CostingCode2    = models.CharField(max_length=50, blank=True)
    ProjectCode     = models.CharField(max_length=50, blank=True)
    FreeText        = models.CharField(max_length=500, blank=True)
    ItemSerialNo    = models.CharField(max_length=100, blank=True)
    # for service app
    Frequency       = models.CharField(max_length=20, blank=True)
    StartDate       = models.CharField(max_length=50, blank=True)
    EndDate         = models.CharField(max_length=50, blank=True)
    IsService 		= models.CharField(max_length=10, default="tNO")
    ReferenceItem   = models.CharField(max_length=255, blank=True)
    ReferenceSerial = models.CharField(max_length=255, blank=True)
