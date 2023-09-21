from django.urls import path, include
from .views import *
from Inspection.Issue import views

urlpatterns = [
    path('issue/create', views.create),
    path('issue/update', views.update),
    path('issue/one', views.one),
    path('issue/all', views.all),
    path('issue/filter', views.filter),
    path('issue/delete', views.delete)
]
