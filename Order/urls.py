from django.urls import path,include
from .views import *
from Order.viewsServiceSupport import *
from .viewsServiceContract import *

urlpatterns = [
    path('create', create),
    path('all', all),
    path('all_filter', all_filter),
    path('all_filter_page', all_filter_page),
	path('delivery', delivery),
	path('delivery_update', delivery_update),
	path('one',one),
	path('read',read),
	path('cancel',cancel),
    path('update',update),
    path('orderamendment_update',orderamendment_update),

    path('addendumcreate', addendumcreate),
    path('addendumall', addendumall),
    path('approve',approve),
    path('pending',pending),
    path('approved',approved),
    path('taptype_create', taptype_create),
	path('taptype_one', taptype_one),
    path('taptype_all', taptype_all),
    path('taptype_update', taptype_update),
	path('taptype_delete', taptype_delete),
    
    path('machinetype_create', machinetype_create),
	path('machinetype_one', machinetype_one),
    path('machinetype_all', machinetype_all),
    path('machinetype_update', machinetype_update),
	path('machinetype_delete', machinetype_delete),
	path('all_po_no', all_po_no),

    path('all_bybp', all_bybp),
    path('sync', sync),
    path('pay_update',pay_update),
    path('bp_list_byorder',bp_list_byorder),
    
    # new apis
    path('order_status',order_status),       #added by millan on 03-10-2022 for order_status api i.e. for pending, approved and rejected order    
    path('remarkshistory', remarksHistory),
    path('item_wise_services', item_wise_services),

    # service contract
    path('create_contract', createContract),
    path('all_service_contacts', allServiceContactList),
    path('order_wise_service_contacts', orderWiseServiceContactList),

    # service
    path('create_service_order', createServiceOrder),
    path('create_amc_order', createAmcOrder),
    path('all_filter_for_service', all_filter_for_service),
    path('stage_all', stage_all),

]
