from django.test import TestCase
from book_management import book
from .models import Author, Book, Tag, BookAndTag, BookAndAuthor


# Create your tests here.

class bookTest(TestCase):
    def setUp(self):
        Book.objects.create(book_id=985236, like=False)
        Author.objects.create(name='infoTestAuthor1')
        Author.objects.create(name='info_test_author_2')
        Tag.objects.create(name='infoTestTag1')
        Tag.objects.create(name='info_test_tag_2')

    def test_book_add(self):
        book.add(874569,['addTestAuthor1','add_test_author_2',],['addTestTag1','add_test_tag_2',])
        self.assertEqual(874569, Book.objects.get(book_id=874569).id)
