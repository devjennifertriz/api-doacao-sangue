from django.urls import path
from .views import *

urlpatterns = [
    path('', PacienteListCreate.as_view()),
    path('<int:pk>/', PacienteDetail.as_view()),
]

