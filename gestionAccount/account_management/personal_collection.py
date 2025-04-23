from gestionAccount.models import Book, AccountToBook
from django.core.paginator import Paginator

def add(account,book_id):
    """
    Add a book into an account personal collection.

    :param account: An instance of the account.
    :param int book_id: The ID of the book that will be added into the account
    :return: A dict that tell the success or failure of the function.
    """
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist as e:
        return {'success': False, 'error': e}

    _, created = AccountToBook.objects.get_or_create(Book_id=book, Account_id=account)
    if created:
        return {'success': True}
    else:
        return {'success': False, 'error': "The book is already in your library."}




def view(account,number = None,page = 0):
    """
    Get all the books in the personal library by default. If a number inputted, it will divide all the books by page.

    :param account: The user you want to access
    :param int number: number of book in a page (facultative)
    :param int page:
    :return: The books in the personal collection of the inputted user.
    """
    book_list = AccountToBook.objects.filter(Account_id=account).values_list('Book_id', flat=True)

    if not number:

        return {
            'books': book_list,
        }

    else:

        paginator = Paginator(book_list, number)
        page_obj = paginator.get_page(page)

        return {
            'books':page_obj,
            'has_previous':page_obj.has_previous(),
            'has_next': page_obj.has_next(),
            'previous_page_number' :page_obj.previous_page_number(),
            'next_page_number' :page_obj.next_page_number(),
            'num_pages':paginator.num_pages
        }
