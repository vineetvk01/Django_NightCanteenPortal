from django.http import HttpResponse
from django.shortcuts import render
from .models import Food_items

def index(request):
    all_foods = Food_items.objects.all()
    context = { 'all_foods' : all_foods }
    return render(request, 'order/index.html',context)
