from django.urls import path, include
from .views import *
from Inspection import views

urlpatterns = [
    path('inspection/create', views.create),
    path('inspection/update', views.update),
    path('inspection/one', views.one),
    path('inspection/all', views.all),
    path('inspection/filter', views.filter),
    path('inspection/delete', views.delete)
]
