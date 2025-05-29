from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Book


@register(Book)
class BookIndex(AlgoliaIndex):
    """
    Algolia index configuration for the Book model.
    """
    # Fields to include in the index
    fields = [
        'title',
        'author', 
        'genre',
        'description',
        'published_year',
        'id',
    ]
    
    # Index settings
    settings = {
        'searchableAttributes': [
            'title',
            'author', 
            'description',
        ],
        'attributesForFaceting': [
            'genre',
            'author', 
            'published_year',
        ],
        'customRanking': [
            'desc(published_year)',
        ],
        'attributesToRetrieve': [
            'title',
            'author',
            'genre', 
            'description',
            'published_year',
            'objectID',
        ],
        'typoTolerance': True,
        'ignorePlurals': True,
        'removeStopWords': True,
    } 