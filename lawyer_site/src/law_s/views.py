from django.shortcuts import render
from .models import Client
from .forms import ClientForm
# Create your views here.

def main(request):
    sent = False
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            sent = True
    else:
        client_form = ClientForm()
    context = {'client_form': client_form, 'sent': sent}
    return render(request, 'base.html', context)


def jacob(request):
    context = {}
    return render(request, "law_s/jacob_handerson.html", context)