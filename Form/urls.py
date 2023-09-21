from django.urls import path, include
from .views import *
from Form import views

urlpatterns = [
    path('form/create', views.create),
    path('form/update', views.update),
    path('form/one', views.one),
    path('form/all', views.all),
    path('form/delete', views.delete)
]
