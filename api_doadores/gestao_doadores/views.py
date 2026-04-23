from django.shortcuts import render
from rest_framework import viewsets, permissions 

from .models import Doador,CriterioDoacao,LocalDoacao,DemonstracaoInteresse
from .serializers import DoadorSerializer,CriterioDoacaoSerializer,LocalDoacaoSerializer,DemonstracaoInteresseSerializer

class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all() 
    serializer_class = DoadorSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

class CriterioDoacaoViewSet(viewsets.ModelViewSet):
    queryset = CriterioDoacao.objects.all() 
    serializer_class = CriterioDoacaoSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LocalDoacaoViewSet(viewsets.ModelViewSet):
    queryset = LocalDoacao.objects.all() 
    serializer_class = LocalDoacaoSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DemonstracaoInteresseViewSet(viewsets.ModelViewSet):
    queryset = DemonstracaoInteresse.objects.all() 
    serializer_class = DemonstracaoInteresseSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

