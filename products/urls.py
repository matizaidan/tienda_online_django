from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),  # Por ejemplo, la URL raíz ('/') apunta a la vista 'home'
    path('catalog/', include('products.catalog.urls')),  # Incluye las URLs de la app 'catalog' dentro de 'products'
]
