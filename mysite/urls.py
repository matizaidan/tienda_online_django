from django.contrib import admin
from django.urls import path, include    # Importa la función include
from django.conf import settings
from django.conf.urls.static import static
from products import views as products_views

urlpatterns = [
    path('', products_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]
