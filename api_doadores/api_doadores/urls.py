from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/doacao/', include('gestao_doadores.urls')),
    
    # Login na api
    path('api-auth/', include('rest_framework.urls')),
]
