from django.contrib import admin
from .models import Author, Book, Tag, BookAndTag, BookAndAuthor

# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BookAndTag)
admin.site.register(BookAndAuthor)