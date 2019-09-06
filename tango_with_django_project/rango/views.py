from django.shortcuts import render
from rango.models import Category


def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    context = {'categories': categories}

    return render(request, 'rango/index.html', context=context)


def about(request):
    context = {'yourname': 'Amos Wang'}

    return render(request, 'rango/about.html', context=context)