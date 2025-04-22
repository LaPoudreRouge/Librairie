from django.db import models
from gestionBook.models import Book
from django.contrib.auth.models import User

# Create your models here.

class AccountToBook(models.Model):
    objects: models.Manager['AccountToBook'] = models.Manager()

    Book_id = models.ForeignKey(Book, on_delete=models.RESTRICT)
    Account_id = models.ForeignKey(User, on_delete=models.CASCADE)