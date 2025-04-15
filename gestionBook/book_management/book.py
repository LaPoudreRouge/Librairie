from typing import List


from gestionBook.models import Author, Tag, Book, BookAndAuthor, BookAndTag

def add(book_id:int, list_authors: List[str], list_tags: List[str]):
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
