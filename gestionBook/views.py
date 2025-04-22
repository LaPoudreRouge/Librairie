from django.http import HttpResponse
from django.shortcuts import render
from authentication.connexion_decorator import require_connexion
from .book_management import book


# Create your views here.

@require_connexion("book.add_w")
def book_add_webpage(request):
    """
    Display the webpage that allow you to input the info on the book you want to add.

    :param request: A POST with the info of the book to add.
    :return: An HTML webpage.
    """
    if request.method == 'POST':

        book_id = request.POST.get('bookID')
        authors_raw = request.POST.get('author').lower()
        tags_raw = request.POST.get('tags').lower()

        # Split authors and tags
        authors_list = [author.strip() for author in authors_raw.split(' ')]
        tags_list = [tag.strip() for tag in tags_raw.split(' ')]

        # register it in the database
        result = book.add(book_id, authors_list, tags_list)

        # check if success or already present
        if result["created"]:
            context = {
                "book_id": book_id,
                "authors": authors_list,
                "tags": tags_list
            }
            return render(request, 'book/add/book_added.html', context)
        else:
            return HttpResponse(f"Book with ID {book_id} already exist.")

    # If the method is not POST, render the form (GET request)
    return render(request, 'book/add/webpage.html')


def book_get_info_webpage(request):
    """
    Display the webpage that allow you to input the book ID you want info on.

    :param request: A POST with the ID of the book you want info on.
    :return: An HTML webpage.
    """
    if request.method == 'POST':
        book_id = request.POST.get('bookID')

        result = book.get_info(book_id)
        if result['success']:
            context = {
                "book_id": book_id,
                "authors": result['authors'],
                "tags": result['tags']
            }
            return render(request,'book/get_info/info_book.html',context)
        else:
            return HttpResponse(f"Error: {result['error']}")
    return render(request, 'book/get_info/ask.html')

def main_hub(request):
    return render(
        request,
        'main_hub/main_hub.html',
        {"logged_in":request.user.is_authenticated}
    )
