from django.urls import path,include
from .views import *

urlpatterns = [
    path('servicecontract/create', create),
    path('servicecontract/all', all),
    path('servicecontract/one', one),
    path('servicecontract/update', update),
    path('servicecontract/servicecontract_filter_key', servicecontract_filter_key),
    path('servicecontract/servicecontract_img_delete', servicecontract_img_delete),

    path('servicecontract/master_create', master_create),
    path('servicecontract/master_all', master_all),
    path('servicecontract/master_one', master_one),
    path('servicecontract/master_update', master_update),
    path('servicecontract/master_filter_key', master_filter_key)
    
]
