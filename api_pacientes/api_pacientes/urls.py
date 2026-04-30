from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from gestao_pacientes.views import PacienteViewSet, SolicitacaoViewSet

router = routers.DefaultRouter()
router.register(r"pacientes", PacienteViewSet, basename="paciente")
router.register(r"solicitacoes", SolicitacaoViewSet, basename="solicitacao")

schema_view = get_schema_view(
    openapi.Info(
        title="API Doacao Sangue - Pacientes",
        default_version="v1",
        description="Documentação da API de Doação de Sangue",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=router.urls,
)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Rotas da Documentação Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

