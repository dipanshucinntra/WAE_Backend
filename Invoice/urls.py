from django.urls import path,include
from .views import *

urlpatterns = [
    path('create', create),
    path('all', all),
    path('all_filter', all_filter),
	path('delivery', delivery),
	path('one',one),
    path('update',update),

    ############# NEW API's ###########
    # new apis
    path('incoming_payments', incoming_payments),
    path('credit_notes', credit_notes),
    path('all_incoming_payments', all_incoming_payments),
    path('payment_collection_dashboard', payment_collection_dashboard),
    path('bp_payment_collection', bp_payment_collection),    
    path('credit_note_dashboard', credit_note_dashboard),
    path('bp_credit_note', bp_credit_note),
    path('pending_payment_collection', pending_payment_collection),
    path('sync_invoice', syncInvoice),
    path('one_receipt', one_receipt),
    path('bp_wise_receipt', bp_wise_receipt),
    path('bp_wise_sold_items', bp_wise_sold_items),
]
