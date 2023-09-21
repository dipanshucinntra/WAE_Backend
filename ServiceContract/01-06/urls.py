from django.urls import path,include
from .views import *

urlpatterns = [
    path('servicecontract/create', create),
    path('servicecontract/all', all),
    path('servicecontract/one', one),
    path('servicecontract/update', update),
    path('servicecontract/delete', delete),
    path('servicecontract/servicecontract_img_delete', servicecontract_img_delete),
]
