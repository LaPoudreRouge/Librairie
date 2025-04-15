from django.urls import  path

from . import  views

urlpatterns = [
    path('add', views.book_add_webpage, name='book.add_w'),
    path('get_info', views.book_get_info_webpage, name='book.get_info_w'),
]