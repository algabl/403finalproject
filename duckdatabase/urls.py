from operator import index
from django.urls import path
from .views import indexPageView, addPageView, editPageView, deletePageView, aboutPageView, searchPageView, confirmationPageView

# the url paths to our pages
app_name = 'duckdatabase'

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("add/", addPageView, name = "add"),
    path("edit/<int:id>", editPageView, name = "edit"),
    path("delete/", deletePageView, name = "delete"),
    path("about/", aboutPageView, name = "about"),
    path("search/", searchPageView, name = "search"),
    path("confirmation/<int:id>", confirmationPageView, name = "confirmation"),
]