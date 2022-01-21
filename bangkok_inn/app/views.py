from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app/index.html")

def menu(request):
    return render(request, "app/menu.html")

def about(request):
    return render(request, "app/about.html")

def order(request):
    return render(request, "app/order.html")
