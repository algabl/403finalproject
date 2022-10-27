from django.http import HttpResponse

def indexPageView(request) :
    # display, update, create, delete
    return HttpResponse('Index')

def addPageView(request) :
    return HttpResponse('Add')

def aboutPageView(request) :
    return HttpResponse('About')

def searchPageView(request) :
    return HttpResponse('Search')

def confirmationPageView(request) :
    return HttpResponse('Confirmation')
