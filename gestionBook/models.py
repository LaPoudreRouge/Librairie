from django.db import models

# Create your models here.

class Book(models.Model):
    objects: models.Manager['Book'] = models.Manager()

    book_id = models.IntegerField(primary_key=True, unique=True)
    like = models.BooleanField()



class Author(models.Model):
    objects: models.Manager['Author'] = models.Manager()

    name = models.CharField(max_length=100, unique=True)
    infos = models.CharField(max_length=5000)



class Tag(models.Model):
    objects: models.Manager['Tag'] = models.Manager()

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=5000)



class BookAndAuthor(models.Model):
    objects: models.Manager['BookAndAuthor'] = models.Manager()

    Book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    Author_id = models.ForeignKey(Author, on_delete=models.RESTRICT)



class BookAndTag(models.Model):
    objects: models.Manager['BookAndTag'] = models.Manager()

    Book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    Tag_id = models.ForeignKey(Tag, on_delete=models.RESTRICT)