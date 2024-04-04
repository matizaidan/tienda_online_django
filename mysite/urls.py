from django.contrib import admin
from django.urls import path, include    # Importa la función include
from django.conf import settings
from django.conf.urls.static import static
from products import views as products_views

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
