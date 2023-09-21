from django.urls import path,include
from Tickets.viewConversation import *
from Tickets.viewDropdown import *
from Tickets.viewParts import *
from Tickets.viewServiceCheckList import *
from Tickets.viewsHistory import *
from .views import *

urlpatterns = [
    # Tickets
    path('tickets/create', create),
    path('tickets/all', all),
    path('tickets/one', one),
    path('tickets/update', update),
    path('tickets/assign', assign_to),
    path('tickets/filter_all', filter_all),
    path('tickets/status_update', status_update),
    path('tickets/accept_reject', accept_reject_ticket),
    path('tickets/ticketstartend', ticket_start_end),
    path('tickets/customerpirupload', customer_pir_upload),
    
    # History
    path('tickets/history/create', createHistory),
    path('tickets/history/all', allHistory),
    path('tickets/history/one', oneHistory),
    path('tickets/history/update', updateHistory),
    path('tickets/history/filter_all', filter_all_history),
    
    # Conversation
    path('tickets/conversation/create', createConversation),
    path('tickets/conversation/all', allConversation),
    # path('tickets/conversation/one', oneConversation),
    # path('tickets/conversation/update', updateConversation),
    path('tickets/conversation/filter_all', filter_all_Conversation),
    
    # Parts
    path('tickets/parts/create', createParts),
    path('tickets/parts/all', allParts),
    path('tickets/parts/one', oneParts),
    path('tickets/parts/update', updateParts),
    path('tickets/parts/filter_all', filter_all_Parts),
    path('tickets/parts/pr_attachments_upload', pr_attachments_upload),
    path('tickets/parts/pr_approve', pr_approve),
    path('tickets/parts/pr_remarks_history', pr_remarks_history),
    
    # ServiceCheckList
    path('tickets/servicechecklist/create', createServiceCheckList),
    path('tickets/servicechecklist/all', allServiceCheckList),
    path('tickets/servicechecklist/one', oneServiceCheckList),
    path('tickets/servicechecklist/update', updateServiceCheckList),
    path('tickets/servicechecklist/filter_all', filter_all_ServiceCheckList),
    
    # dropdowns
    path('tickets/dropdowns/type', allType),
    path('tickets/dropdowns/status', allStatus),
    path('tickets/dropdowns/ticketstatus', allTicketStatus),
    path('tickets/dropdowns/priority', allPriority),
    path('tickets/dropdowns/zone', allZone),

    # filter apis
    path('tickets/item_wise_tickets', item_wise_tickets),
    path('tickets/tickets_dashboard', tickets_dashboard),
    path('tickets/filterbykey', filterbykey),
    path('tickets/searchintickets', searchInTickets),
    path('tickets/tickets_bp_dashboard', tickets_bp_dashboard),

]
