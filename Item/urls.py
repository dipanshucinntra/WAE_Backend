from django.urls import path,include
from .views import *

urlpatterns = [
    path('all', all),
    path('all1', all1),
    path('one',one),
    path('tax_all', tax_all),
    path('distributionlist',distributionlist),
    
    #added by millan on 03-November-2022
    path('create',create),
    path('update',update),
    path('delete',delete),
    #added by millan on 03-November-2022

    ##################### New Url By [DK]############
    path('all_pending', all_pending),
    path('itemremarksHistory',itemremarksHistory),
    path('approve',approve),
    ##################### New Url By [DK]############
    
    path('all_filter',all_filter),
    path('all_item_group',all_item_group),

    path('item_count',item_count),
    path('searchinitems',searchInItems),
]
