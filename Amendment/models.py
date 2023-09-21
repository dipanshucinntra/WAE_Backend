from django.db import models

# Create your models here.

class Amendment(models.Model):
    order_id = models.CharField(max_length=200, blank=True)
    ops_revision = models.CharField(max_length=200, blank=True)
    client_name = models.CharField(max_length=200, blank=True)
    ops_number = models.CharField(max_length=200, blank=True)
    amendment = models.CharField(max_length=200, blank=True)
    reason = models.CharField(max_length=200, blank=True)
    open_date = models.CharField(max_length=200, blank=True)
    close_date = models.CharField(max_length=200, blank=True)
    created_by = models.CharField(max_length=200, blank=True)
    approved_by = models.CharField(max_length=200, blank=True)
    approval_status = models.CharField(max_length=200, blank=True, default="Pending")
    machine_sp_type= models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class AmendmentOrderStatusRemarks(models.Model):
    Amendment_id    = models.CharField(max_length=5, blank=True)
    SalesEmployeeCode= models.CharField(max_length=5, blank=True)
    Status          = models.CharField(max_length=50, blank=True)
    Remarks         = models.CharField(max_length=255, blank=True)
    Datetime        = models.DateTimeField(auto_now_add=True)