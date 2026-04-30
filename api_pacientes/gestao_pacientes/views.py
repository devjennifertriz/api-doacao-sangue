from django.shortcuts import render
from .models import Paciente, SolicitacaoDoacao
from .serializers import PacienteSerializer, SolicitacaoDoacaoSerializer
from rest_framework import viewsets, permissions

# Create your views here.


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.AllowAny]

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoDoacao.objects.all()
    serializer_class = SolicitacaoDoacaoSerializer
    permission_classes = [permissions.AllowAny]