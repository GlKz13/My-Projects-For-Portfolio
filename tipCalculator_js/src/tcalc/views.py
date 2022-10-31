from django.shortcuts import render
from . forms import TipCalcForm

# Create your views here.

def main(request):
    form = TipCalcForm()
    context = {'form': form}
    return render(request, 'base.html', context)



