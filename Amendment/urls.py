from django.urls import path,include
from .views import *
from BusinessPartner import views, viewsBPBranch, viewsBPEmployee, viewsBPDepartment, viewsBPPosition, viewsBPCurrency

urlpatterns = [
    path('create', create),
    path('all_filter_page', all_filter_page),
    path('update', update),
    # path('amendment_status', amendment_status),
    path('amendmentremarksHistory',amendmentremarksHistory),
    path('approve',approve)
    #path('all', all)
]