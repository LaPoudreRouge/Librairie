from typing import List


from gestionBook.models import Author, Tag, Book, BookAndAuthor, BookAndTag

def add(book_id:int, list_authors: List[str], list_tags: List[str]):
    """
    Add a book into the database. Additional info like authors and tags can be added too.
    :param book_id: The ID of the book.
    :param list_authors: A list of all the authors of the book.
    :param list_tags: A list of all the tags of the book
    'created': If the book has been created.
    :returns (dict):  Return a dict confirming if it worked or not:
        - 'created': If the book has been created.
    :rtype: dict
    """
    book, created = Book.objects.get_or_create(book_id=book_id,like=False)
    if not created:
        return {'created':False}

    authors_to_add = []
    for author in list_authors:
        author_obj, _ = Author.objects.get_or_create(name=author)
        authors_to_add.append(author_obj)

    tags_to_add=[]
    for tag in list_tags:
        tag_obj, _ = Tag.objects.get_or_create(name=tag)
        tags_to_add.append(tag_obj)

    for tag_to_add in tags_to_add:
        BookAndTag.objects.create(Book_id=book, Tag_id=tag_to_add)

    for author_to_add in authors_to_add:
        BookAndAuthor.objects.create(Book_id=book, Author_id=author_to_add)

    return {'created':True}


def get_info(book_id):
    """
    Gets all the infos linked to this book. (like, authors, tags)
    :param book_id: The ID of the book you want info on.
    :returns (dict): A dictionary containing if the function succeeded and the infos asked:
        - 'success' (bool): A boolean indicating if the operation was successful.
        - 'like' (bool): If the book has been liked.
        - 'authors' : A list of authors associated with the book.
        - 'tags' (list of str): A list of tags related to the book.
    :rtype: dict
    """
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist as e:
        return {'success':False,'error':e}
    try:
        authors = Author.objects.filter(bookandauthor__Book_id=book).values_list('name', flat=True)
        tags = Tag.objects.filter(bookandtag__Book_id=book).values_list('name', flat=True)
        return {'success': True, 'like': book.like, 'authors': authors, 'tags': tags}
    except Exception as e:
        return {'success':False,'error':e}
