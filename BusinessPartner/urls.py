from django.urls import path,include
from .views import *
from BusinessPartner import views,viewsBPUser, viewsBPBranch, viewsBPEmployee, viewsBPDepartment, viewsBPPosition, viewsBPCurrency

urlpatterns = [
    path('businesspartner/create', create),
    path('businesspartner/all', all),
    path('businesspartner/all_filter_page', all_filter_page),
    path('businesspartner/all_bp', all_bp),
    path('businesspartner/one', one),
    path('businesspartner/sync', sync),
    path('businesspartner/points', points),
    path('businesspartner/update', update),
    path('businesspartner/delete', delete),
    path('businesspartner/branchbybp', branchbybp),
    
    path('businesspartner/branch/create', viewsBPBranch.create),
    path('businesspartner/branch/one', viewsBPBranch.one),
    path('businesspartner/branch/all', viewsBPBranch.all),
    path('businesspartner/branch/update', viewsBPBranch.update),
    path('businesspartner/branch/delete', viewsBPBranch.delete),
    
    path('businesspartner/employee/create', viewsBPEmployee.create),
    path('businesspartner/employee/one', viewsBPEmployee.one),
    path('businesspartner/employee/all', viewsBPEmployee.all),
    path('businesspartner/employee/update', viewsBPEmployee.update),
    path('businesspartner/employee/delete', viewsBPEmployee.delete),

    path('businesspartner/user/create', viewsBPUser.create),
    path('businesspartner/user/one', viewsBPUser.one),
    path('businesspartner/user/all', viewsBPUser.all),
    path('businesspartner/user/update', viewsBPUser.update),
    path('businesspartner/user/delete', viewsBPUser.delete),
    path('businesspartner/user/login', viewsBPUser.login),
    path('businesspartner/user/dashboard', viewsBPUser.dashboard),
    
    path('businesspartner/department/create', viewsBPDepartment.create),
    path('businesspartner/department/one', viewsBPDepartment.one),
    path('businesspartner/department/all', viewsBPDepartment.all),
    path('businesspartner/department/update', viewsBPDepartment.update),
    path('businesspartner/department/delete', viewsBPDepartment.delete),
    path('businesspartner/department/sync', viewsBPDepartment.sync),
    
    path('businesspartner/position/create', viewsBPPosition.create),
    path('businesspartner/position/one', viewsBPPosition.one),
    path('businesspartner/position/all', viewsBPPosition.all),
    path('businesspartner/position/update', viewsBPPosition.update),
    path('businesspartner/position/delete', viewsBPPosition.delete),
        path('businesspartner/position/sync', viewsBPPosition.sync),
    
    path('businesspartner/currency/create', viewsBPCurrency.create),
    path('businesspartner/currency/one', viewsBPCurrency.one),
    path('businesspartner/currency/all', viewsBPCurrency.all),
    path('businesspartner/currency/update', viewsBPCurrency.update),
    path('businesspartner/currency/delete', viewsBPCurrency.delete),
    
    #added by millan on 11-10-2022
    path('businesspartner/monthlySales', monthlySales),  
    path('businesspartner/employee_target', employee_target), 
    path('businesspartner/target_anu_ach', target_anu_ach), 

    #added by millan on 01-11-2022
    path('businesspartner/all_bpEmployee', all_bpEmployee),  
]
