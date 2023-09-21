from django import forms
from .models import ServiceContract

class ServiceContractForm(forms.ModelForm):
    class Meta:
        model = ServiceContract
        fields = "__all__"
