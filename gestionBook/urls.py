from django.urls import  path

from . import  views

urlpatterns = [
    path('interface', views.add_book_webpage,name='add_book_w'),
]