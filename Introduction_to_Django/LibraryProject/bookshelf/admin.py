from django.contrib import admin
from .models import Book

# Custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display
    search_fields = ('title', 'author')                     # search by title or author
    list_filter = ('publication_year',)                     # filter by publication year

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)
