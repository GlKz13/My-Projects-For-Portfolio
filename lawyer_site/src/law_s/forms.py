from .models import Client
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone']
        widgets = {
            'phone': forms.TextInput()
        }