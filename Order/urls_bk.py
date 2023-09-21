from django.urls import path,include
from .views import *

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
	path('machinetype_delete', machinetype_delete)

]
