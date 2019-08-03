from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def shop(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def home(request):
    return render(request, 'home.html')
