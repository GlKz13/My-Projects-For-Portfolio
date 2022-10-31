from django import forms

class TipCalcForm(forms.Form):
    price = forms.CharField(label='Price', widget=forms.TextInput(
        attrs={'id':'BillTotallInput', 'placeholder': '0.00', 'onkeyup': 'BillTotalInputUpdate()'}))
    tip_amount = forms.CharField(label='Tip amount', widget=forms.TextInput(
        attrs={'id':'tipInput', 'placeholder': '10', 'onkeyup': 'BillTotalInputUpdate()'}))
