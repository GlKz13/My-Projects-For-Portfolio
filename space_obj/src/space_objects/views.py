from django.shortcuts import render, get_object_or_404
from .models import *
from  .forms import *


cats = Category.objects.all()
objects = SpaceObject.objects.all()
form = Subscribe()
sidebar = []
# Create your views here.

def show_main_page(request):

    #objects = SpaceObject.objects.all()
    #cats = Category.objects.all()

    if request.method == "POST":
        email_form = Subscribe(data=request.POST)
        if email_form.is_valid():
            cd = email_form.cleaned_data
            sub = Email.objects.create(email=cd['email'], name=cd['name'])
            send = True
    else:
        email_form = Subscribe()
        send = None

    context = {'sp_objects': objects,
                'cats': cats,
                'form': email_form,
               'send': send}
    return render(request, 'base.html', context)


def category_page(request, cat_slug):
    objs = SpaceObject.objects.filter(cat__slug=cat_slug)
    cat = Category.objects.get(slug=cat_slug)
    context = {'objs': objs,
               'cat': cat,
               'cats': cats,
               'form': form}
    return render(request, 'space_objects/show_category.html', context)



def obj_content(request, obj_slug):
    obj = SpaceObject.objects.get(slug=obj_slug)
    context = {'obj': obj,
                'cats': cats,
                'form': form}
    return render(request, 'space_objects/object_content.html', context)
