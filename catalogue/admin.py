from django.contrib import admin
from django.db.models import Case, When
from algoliasearch_django import raw_search

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for Book model with Algolia search integration.
    """
    list_display = ['title', 'author', 'genre', 'published_year', 'created_at']
    list_filter = ['genre', 'published_year', 'created_at']
    search_fields = ['title', 'author', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'genre', 'description', 'published_year')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_search_results(self, request, queryset, search_term):
        """
        Override default search to use Algolia when search_term is provided.
        This respects Algolia's relevance ranking and typo tolerance.
        """
        if not search_term:
            # No search term, return default behavior
            return super().get_search_results(request, queryset, search_term)
        
        try:
            # Use Algolia raw search
            response = raw_search(Book, search_term)
            
            # Extract object IDs from Algolia response
            object_ids = [hit['objectID'] for hit in response['hits']]
            
            if object_ids:
                # Filter queryset to only include objects found by Algolia
                # Preserve the order returned by Algolia
                preserved_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(object_ids)])
                queryset = queryset.filter(pk__in=object_ids).order_by(preserved_order)
                
                # Return with use_distinct=False since we're handling ordering manually
                return queryset, False
            else:
                # No results from Algolia
                return queryset.none(), False
                
        except Exception as e:
            # Fallback to default Django search if Algolia fails
            print(f"Algolia search failed: {e}")
            return super().get_search_results(request, queryset, search_term)
