from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('search/', views.search, name='search'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
] 