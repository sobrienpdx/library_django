from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'library_app/index.html')
    return HttpResponse('ok')

# Create your views here.
