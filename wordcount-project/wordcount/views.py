from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})


def eggs(request):
    return HttpResponse('Eggs are great!!!!')

def count(request):
    return render(request, 'count.html')