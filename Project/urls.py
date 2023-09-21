from django.urls import path,include
from .views import *

urlpatterns = [
    path('create', create),
    path('all', all),
    path('allbycp', allbycp),
    path('one',one),
    path('update', update),
    path('delete', delete),    
    path('project_all', project_all), # added by millan on 01-November-2022

    path('master_create', master_create),    
    path('master_all', master_all),   
    path('master_one',master_one),
    path('master_update', master_update),
    path('stage_update', stage_update),
    path('stage_complete', stage_complete),    
    path('master_project_all', master_project_all),
    path('project_filter', project_filter),
    path('master_project_filter', master_project_filter),
    path('project_filter_key', project_filter_key),
    path('stage_all', stage_all),
    path('stage_all_bytype', stage_all_bytype),
    path('stage_one', stage_one),
    path('static_stage_all', static_stage_all)
]
