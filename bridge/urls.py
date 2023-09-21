"""bridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead/', include('Lead.urls')),
    path('activity/', include('Activity.urls')),
    path('notification/', include('Notification.urls')),
    path('', include('Countries.urls')),
    path('', include('Countries.urls')),
    path('employee/', include('Employee.urls')),
    path('quotation/', include('Quotation.urls')),
    path('order/', include('Order.urls')),
    path('draftorder/', include('DraftOrder.urls')),
    path('invoice/', include('Invoice.urls')),
    path('item/', include('Item.urls')),
    path('category/', include('Category.urls')),
    path('industries/', include('Industries.urls')),
    path('paymenttermstypes/', include('PaymentTermsTypes.urls')),
    path('company/', include('Company.urls')),
    path('branch/', include('Branch.urls')),
    path('', include('Opportunity.urls')),
    path('', include('Tender.urls')),
    path('', include('BusinessPartner.urls')),
    path('', include('Campaign.urls')),
    path('project/', include('Project.urls')),
    path('attachment/', include('Attachment.urls')),
    path('clientbankdetails/', include('ClientBankDetails.urls')),
    path('amendment/', include('Amendment.urls')),
    path('', include('Payment.urls')),
    ########################### NEW URLS ADD BY DIPANSHU ########################
    path('announcement/', include('Announcement.urls')),
    path('delivery/', include('Delivery.urls')),
    path('dropdown/', include('DropDown.urls')),
    path('', include('Feedback.urls')),
    path('', include('Form.urls')),
    path('', include('Inspection.urls')),
    path('inspection/', include('Inspection.Issue.urls')),
    path('inspection/', include('Inspection.IssueCategory.urls')),
    path('', include('ItemsPIR.urls')),
    path('', include('ServiceContract.urls')),
    path('tdquotation/', include('TenderQuotation.urls')),
    path('', include('Tickets.urls')),
]
