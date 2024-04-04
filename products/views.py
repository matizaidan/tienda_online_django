from django.shortcuts import render
from products.catalog.models import Product, Category

def home(request):
    # Obtener todas las categorías
    categories = Category.objects.all()
    # Renderizar la plantilla 'home.html' y pasar las categorías como contexto
    return render(request, 'home.html', {'categories': categories})
