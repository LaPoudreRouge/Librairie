from django.urls import path

from . import  views

urlpatterns = [
    path("personal_collection/add",views.persColl_add_webpage)
]