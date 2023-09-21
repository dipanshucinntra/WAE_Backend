from django.urls import path,include
from .views import *

urlpatterns = [
    # path('create', create),
    path('all', all),
    path('all_filter', all_filter),
	# path('delivery', delivery),
	path('one',one),
    # path('update',update),

    # filter list
    path('bp_list', bp_list),
    path('bp_wise', bp_wise_delivery),
    path('bp_wise_items', bp_wise_delivery_items),
    path('itemdetails', itemdetails_by_serialno),
    path('bp_contact_list', bp_contact_person_list),
    path('alldeliveryitems', allDeliveryItems),
    
    # other apis
    path('delivery_attachments_upload', delivery_attachments_upload),
]
