from django.urls import path,include
from .views import *
urlpatterns = [
    path('opportunity/create', create),
    path('opportunity/all', all),
    path('opportunity/all_opp', all_opp),
    path('opportunity/all_filter', all_filter),
    path('opportunity/all_filter_page', all_filter_page),
    path('opportunity/one', one),
    path('opportunity/update', update),
    path('opportunity/change_stage', change_stage),
    path('opportunity/complete', complete),
    path('opportunity/fav', fav),

    path('stage/all', all_stage),
    path('stage/one', one_stage),
    path('stage/stage_detail', stage_detail),
    path('stage/create', create_stage),
    path('stage/complete', stage_complete),
    path('line/all', all_line),
    path('line/one', one_line),

    
    path('opportunity/excelDownload', excelDownload),
    path('opportunity/opp_status_update', opp_status_update),
    
    path('opportunity/initiation/create', initiation_create),
    path('opportunity/initiation/one', initiation_one),
    path('opportunity/initiation/update', initiation_update),
    
    path('opportunity/rfq/one', rfq_one),
    path('opportunity/rfq/update', rfq_update),
    path('opportunity/presite/one', presite_one),
    path('opportunity/presite/update', presite_update),
    path('opportunity/site/one', site_one),
    path('opportunity/site/update', site_update)

]
