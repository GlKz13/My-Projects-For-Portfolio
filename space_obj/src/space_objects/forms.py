from django import  forms
from . models import *

class Subscribe(forms.Form):
    name = forms.CharField(max_length=20, label='Ваше имя')
    email = forms.EmailField(label='Ваш e-mail')

