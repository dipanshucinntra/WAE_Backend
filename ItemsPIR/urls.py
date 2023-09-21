from django.urls import path,include
from .views import *

urlpatterns = [
    path('itempir/create', create),
    path('itempir/all', all),
    path('itempir/all_filter', all_filter),
    # path('itempir/one',one),
    path('itempir/update', update),

]
