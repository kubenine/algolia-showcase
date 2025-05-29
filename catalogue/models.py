from django.db import models

# Create your models here.

class Book(models.Model):
    """
    Book model for the BookHub catalogue.
    """
    title = models.CharField(max_length=200, help_text="Book title")
    author = models.CharField(max_length=100, help_text="Author name")
    genre = models.CharField(max_length=50, help_text="Book genre")
    description = models.TextField(help_text="Book description/blurb")
    published_year = models.IntegerField(help_text="Year of publication")
    
    # Additional metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_year', 'title']
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.published_year})"
