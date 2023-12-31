from django.db import models  

class ServiceContract(models.Model):
    OrderID = models.CharField(max_length=100, blank=True)
    ProjectID = models.CharField(max_length=100, blank=True)
    MNo = models.CharField(max_length=100, blank=True)
    ProductSerialNo = models.CharField(max_length=250, blank=True)
    ProductCate = models.CharField(max_length=250, blank=True)
    ProductSubCate = models.CharField(max_length=250, blank=True)
    ServiceContractID = models.CharField(max_length=100, blank=True)
    ServiceContractType = models.CharField(max_length=100, blank=True)
    ContractPersoneName = models.CharField(max_length=150, blank=True)
    ContractPersoneNumber = models.CharField(max_length=50, blank=True)
    CountryCode = models.CharField(max_length=50, blank=True)
    Frequency = models.CharField(max_length=50, blank=True)
    FromDate = models.CharField(max_length=50, blank=True)
    ToDate = models.CharField(max_length=50, blank=True)
    CheckList = models.CharField(max_length=250, blank=True)
    CardCode = models.CharField(max_length=100, blank=True)
    BPName = models.CharField(max_length=250, blank=True)
    Remarks = models.TextField(blank=True)
    ServiceContractOwner = models.IntegerField(default=0)
    ServiceContractOwnerName = models.CharField(max_length=150, blank=True)
    SiteEngineerAssigned = models.IntegerField(default=0)
    SiteEngineerAssignedName = models.CharField(max_length=150, blank=True)
    ContractType = models.CharField(max_length=100, blank=True)
    Status = models.IntegerField(default=0)
    ServiceContractsItem = models.TextField(blank=True)
    ServiceItem = models.TextField(blank=True)
