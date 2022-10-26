from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Index')

def contactPageView(request) :
    return HttpResponse('Contact')

def aboutPageView(request) :
    return HttpResponse('About')

def searchPageView(request) :
    return HttpResponse('Search')