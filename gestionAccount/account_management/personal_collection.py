from gestionAccount.models import Book, AccountToBook

def add(account,book_id):
    """
    Add a book into an account personal collection.

    :param int account_id: The ID of the account.
    :param int book_id: The ID of the book that will be added into the account
    :return:
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
