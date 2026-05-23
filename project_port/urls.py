from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Todas as requisições que começarem com /api/ serão delegadas ao router do portifolio
    path('api/', include('portifolio.urls')),
]

# Configuração essencial para o Django servir os arquivos de mídia (como as thumbnails dos projetos) 
# durante o desenvolvimento local.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)