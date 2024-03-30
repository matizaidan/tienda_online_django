from django.contrib import admin
from django.urls import path, include    # Importa la función include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
