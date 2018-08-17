from django.urls import path
from . import views

library_app = 'library_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    
]
