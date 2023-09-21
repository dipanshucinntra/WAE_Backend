from django.urls import path,include
from .views import *

urlpatterns = [
    path('create', create),
    path('all', all),
    path('all_filter', all_filter),
	path('one',one),
	path('cancel',cancel),
	path('delete',delete),
    path('update',update),
    path('addendumcreate', addendumcreate),
    path('addendumall', addendumall),

]
