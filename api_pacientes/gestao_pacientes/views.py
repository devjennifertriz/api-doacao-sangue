from django.shortcuts import render
from rest_framework import generics
from .models import Paciente, SolicitacaoDoacao
from .serializers import PacienteSerializer, SolicitacaoDoacaoSerializer

# Create your views here.

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class SolicitacaoDoacaoListCreate(generics.ListCreateAPIView):
    queryset = SolicitacaoDoacao.objects.all()
    serializer_class = SolicitacaoDoacaoSerializer

class SolicitacaoDoacaoDetail(generics.RetrieveAPIView):
    queryset = SolicitacaoDoacao.objects.all()
    serializer_class = SolicitacaoDoacaoSerializer