from lib2to3.fixes.fix_input import context

from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'

    }
    return render(request, 'main/index.html', context)
def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин мебели "HOME" предлагает стильную и качественную мебель для дома и офиса. В ассортименте – удобные диваны, кровати, шкафы и столы от ведущих производителей. Мы гарантируем долговечность каждой покупки и помогаем подобрать мебель, создавая уют в вашем интерьере.'

    }
    return render(request, 'main/about.html', context)
