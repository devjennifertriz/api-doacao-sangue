from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Doador, CriterioDoacao,RegistrarDoacao
from .serializers import (
    DoadorSerializer,
    CriterioDoacaoSerializer,
    RegistrarDoacaoSerializer,
)

class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer
    permission_classes = [permissions.AllowAny]
    
class CriterioDoacaoViewSet(viewsets.ModelViewSet):
    queryset = CriterioDoacao.objects.all()
    serializer_class = CriterioDoacaoSerializer
    permission_classes = [permissions.AllowAny]
       
class RegistrarDoacaoViewSet(viewsets.ModelViewSet):
    queryset = RegistrarDoacao.objects.all()
    serializer_class = RegistrarDoacaoSerializer
    permission_classes = [permissions.AllowAny]
    

