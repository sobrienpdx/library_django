from django.urls import path
from . import views

app_name = 'library_app' # for namespacing
urlpatterns = [
	path('', views.index, name='index'),
	path('search_books/', views.search_books, name='search_books'),
	path('checkout/', views.checkout, name='checkout'),
	path('my_checkouts/', views.my_checkouts, name='my_checkouts')
]
