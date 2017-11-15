from django.http import HttpResponse
from django.shortcuts import render
from .models import Food_items

def index(request):
    all_foods = Food_items.objects.all()
    context = { 'all_foods' : all_foods }
    return render(request, 'order/index.html',context)

def makeorder(request):
    all_foods = Food_items.objects.all()
    context = { 'all_foods' : all_foods }
    return render(request, 'order/makeorder.html', context)

def payorder(request):
    all_foods = Food_items.objects.all()
    context = { 'all_foods' : all_foods }
    return render(request, 'order/payorder.html', context)

def doneorder(request):
    all_foods = Food_items.objects.all()
    context = { 'all_foods' : all_foods }
    return render(request, 'order/doneorder.html', context)
