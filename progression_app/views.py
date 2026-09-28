from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

# Create your views here.


def arithmetic_sum(request: HttpRequest):
    a1, d, n = float(request.GET.get('a1')), float(request.GET.get('d')), int(request.GET.get('n'))

    S_n = (2*a1 + d*(n-1)) * n / 2
    
    return HttpResponse(f"Сума перших {n} членів арифметичної прогресії: {S_n}")