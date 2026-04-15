from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('gestao_pacientes/', include('gestao_pacientes.urls')),
]
