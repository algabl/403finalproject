from operator import index
from django.urls import path
from .views import indexPageView, aboutPageView, addPageView, searchPageView, confirmationPageView

# the url paths to our pages

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about", aboutPageView, name = "about"),
    path("add", addPageView, name = "add"),
    path("search", searchPageView, name = "search"),
    path("confirmation", confirmationPageView, name = "confirmation"),
]