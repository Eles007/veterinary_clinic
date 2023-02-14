from django.shortcuts import render
from .models import Price, GroupPrice,Article


def index(request):
    return render(request, 'main_functions_website/index.html')


def price(request):
    price = Price.objects.all()
    title = price.values_list('group_price__name',flat=True).order_by('group_price__position').distinct()

    context = {
        'title': title,
        'price': price,
        }

    return render(request, 'main_functions_website/price.html', context)

def article(request):
    content = Article.objects.all()
    context = {
        'content':content,
    }
    return render(request, 'main_functions_website/article.html',context)
