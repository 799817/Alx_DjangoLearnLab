from django.contrib import admin
from .models import Book, Author  # Import your models

# Register your models
admin.site.register(Book)
admin.site.register(Author)
