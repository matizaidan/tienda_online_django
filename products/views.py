from django.shortcuts import render

def home(request):
    # Aquí puedes incluir la lógica necesaria para la vista 'home'
    return render(request, 'products/home.html')
