from django.urls import path,include
from .views import *
from Quotation.viewsServiceSupport import *

urlpatterns = [
    path('create', create),
    path('all', all),
    path('all_filter', all_filter),
    path('one',one),
    path('update',update),
    path('cancel',cancel),
    path('fav',fav),
    path('approve',approve),
    path('pending',pending),
    path('approved',approved),

    path('rejected', rejected),
    path('all_filter_page', all_filter_page),
    path('remarkshistory', remarksHistory),    
    path('pi_attachments_upload', pi_attachments_upload),
    path('pi_attachments_delete', pi_attachments_delete),  
    path('create_service_quotation', createServiceQuotation),
    path('all_filter_for_service', all_filter_for_service),
]
