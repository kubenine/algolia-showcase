from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from algoliasearch_django import raw_search

from .models import Book


def book_list(request):
    """
    Display a list of all books.
    """
    books = Book.objects.all()[:20]  # Limit to 20 for demo
    return render(request, 'catalogue/book_list.html', {
        'books': books
    })


def search(request):
    """
    InstantSearch.js powered search page.
    """
    context = {
        'algolia_app_id': settings.ALGOLIA.get('APPLICATION_ID', ''),
        'algolia_search_key': settings.ALGOLIA.get('SEARCH_KEY', ''),
    }
    return render(request, 'catalogue/search.html', context)


def book_detail(request, book_id):
    """
    Display details for a specific book.
    """
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'catalogue/book_detail.html', {
        'book': book
    })


def api_search(request):
    """
    API endpoint for search functionality (optional fallback).
    """
    query = request.GET.get('q', '')
    
    if not query:
        return JsonResponse({'hits': []})
    
    try:
        # Use Algolia raw search
        response = raw_search(Book, query)
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'hits': []
        }, status=500)
