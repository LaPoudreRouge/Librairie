from django.urls import path

from . import  views

urlpatterns = [
    path("personal_collection/add",views.persColl_add_webpage,name = "personal_collection.add_w"),
    path("personal_collection/view",views.persColl_view_webpage, name = "personal_collection.view_w"),
]