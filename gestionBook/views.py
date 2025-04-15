from django.http import HttpResponse
from django.shortcuts import render

from . import input_book as imbk
# Create your views here.

# send ======================================
def add_book_webpage(request):
    if request.method == 'POST':

        book_id = request.POST.get('bookID')
        authors_raw = request.POST.get('author')
        tags_raw = request.POST.get('tags')

        # Split authors and tags
        authors_list = [author.strip() for author in authors_raw.split(' ')]
        tags_list = [tag.strip() for tag in tags_raw.split(' ')]

        # register it in the database
        result = imbk.input_book(book_id, authors_list, tags_list)

        # check if success or already present
        if result["book"]=='already exist':
            return HttpResponse(f"Book with ID {book_id} already exist.")
        else:
            context = {
                "book_id": book_id,
                "authors": authors_list,
                "tags": tags_list
            }
            return render(request, 'add_book/book_added.html',context)

    # If the method is not POST, render the form (GET request)
    return render(request, 'add_book/webpage.html')

