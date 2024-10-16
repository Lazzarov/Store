from lib2to3.fixes.fix_input import context

from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home Page',
        'content': 'Главная страница'

    }
    return render(request, 'main/index.html', context)
def about(request):
    return HttpResponse("about page")