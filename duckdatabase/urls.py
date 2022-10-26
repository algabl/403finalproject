from operator import index
from django.urls import path
from .views import indexPageView, aboutPageView, contactPageView, searchPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about", aboutPageView, name = "about"),
    path("contact", contactPageView, name = "contact"),
    path("search", searchPageView, name = "search"),
]