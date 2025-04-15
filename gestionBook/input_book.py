from typing import List

from .models import Author, Tag, Book, BookAndAuthor, BookAndTag

def input_book(book_id:int, list_authors: List[str], list_tags: List[str]):
    book, created = Book.objects.get_or_create(book_id=book_id,like=False)
    if not created:
        return {'book':'already exist'}

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

    return {'book': 'created'}

