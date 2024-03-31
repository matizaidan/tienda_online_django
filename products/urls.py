from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Incluir otras partes de la aplicación 'products' aquí
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)