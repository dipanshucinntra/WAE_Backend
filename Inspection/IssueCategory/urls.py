from django.urls import path, include
from .views import *
from Inspection.IssueCategory import views

urlpatterns = [
    path('issuecategory/create', views.create),
    path('issuecategory/update', views.update),
    path('issuecategory/one', views.one),
    path('issuecategory/all', views.all),
    path('issuecategory/filter', views.filter),
    path('issuecategory/delete', views.delete)
]
