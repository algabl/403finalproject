from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Duck, Owner, Color
from django.urls import reverse
from dateutil import relativedelta
from .forms import *

# all of the pages that we plan on using in our project

def indexPageView(request) :
    ducks = Duck.objects.all()
    context = {
        'ducks' : ducks
    }
    return render(request, 'duckdatabase/index.html', context)

def addPageView(request) :
    form = DuckForm()
    color_form = ColorForm()
    owner_form = OwnerForm()

    if request.method == 'POST' and "duck_form" in request.POST:
        form = DuckForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return indexPageView(request)
    elif request.method =='POST' and "color_form" in request.POST:
        submit_form = ColorForm(request.POST, request.FILES)
        submit_form.save()
    elif request.method =='POST' and "owner_form" in request.POST:
        submit_form = OwnerForm(request.POST, request.FILES)
        submit_form.save()
    context = {
        'form' : form,
        'color_form' : color_form,
        'owner_form' : owner_form
    }
    return render(request, 'duckdatabase/add.html', context)

def editPageView(request, id) :
    duck = Duck.objects.get(id=id)
    color_form = ColorForm()
    owner_form = OwnerForm()

    if request.method =='POST' and "duck_form" in request.POST:
        submit_form = DuckForm(request.POST, request.FILES, instance=duck)
        if submit_form.is_valid() :
            submit_form.save()
    elif request.method =='POST' and "color_form" in request.POST:
        submit_form = ColorForm(request.POST, request.FILES)
        submit_form.save()
    elif request.method =='POST' and "owner_form" in request.POST:
        submit_form = OwnerForm(request.POST, request.FILES)
        submit_form.save()
    form = DuckForm(instance=duck)
    context = {
        'form' : form,
        'duck': duck,
        'owner_form': owner_form,
        'color_form': color_form
    }
    return render(request, 'duckdatabase/edit.html', context)

def deletePageView(request) :
    return render(request, 'duckdatabase/delete.html')

def aboutPageView(request) :
    return render(request, 'duckdatabase/about.html')

def searchPageView(request) :
    context = {

    }
    return render(request, 'duckdatabase/search.html', context)

def confirmationPageView(request, id) :
    duck = Duck.objects.get(id=id)
    if request.method == 'POST' and 'yes' in request.POST :
        duck = Duck.objects.get(id=id)
        duck.delete()
        return indexPageView(request)
    elif request.method == 'POST' and 'no' in request.POST :
        return indexPageView(request)
    context = {
        'duck': duck
    }
    return render(request, 'duckdatabase/confirmation.html', context)
