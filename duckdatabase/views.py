from django.shortcuts import render
from django.http import HttpResponse

# all of the pages that we plan on using in our project

def indexPageView(request) :
    return render(request, 'duckdatabase/index.html')

def addPageView(request) :
    return render(request, 'duckdatabase/add.html')

def editPageView(request) :
    return render(request, 'duckdatabase/edit.html')

def deletePageView(request) :
    return render(request, 'duckdatabase/delete.html')

def aboutPageView(request) :
    return render(request, 'duckdatabase/about.html')

def searchPageView(request) :
    return render(request, 'duckdatabase/search.html')

def confirmationPageView(request) :
    return render(request, 'duckdatabase/confirmation.html')
