from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Store author's name

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Link to Author

    def __str__(self):
        return self.title
