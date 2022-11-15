from django.shortcuts import render
from django.http import HttpResponse

# all of the pages that we plan on using in our project

def indexPageView(request) :
    return render(request, 'duckdatabase/index.html')

def addPageView(request) :
    return HttpResponse('Add')

def aboutPageView(request) :
    return HttpResponse('About')

def searchPageView(request) :
    return HttpResponse('Search')

def confirmationPageView(request) :
    return HttpResponse('Confirmation')
