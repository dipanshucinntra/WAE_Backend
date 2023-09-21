from django.urls import path, include
from .views import *
from Feedback import views

urlpatterns = [
    path('feedback/create', views.create),
    path('feedback/update', views.update),
    path('feedback/one', views.one),
    path('feedback/all', views.all),
    path('feedback/all_filter', views.all_filter),
    path('feedback/delete', views.delete)
]
