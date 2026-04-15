from django.shortcuts import render
from rest_framework import generics
from .models import Paciente
from .serializers import PacienteSerializer

# Create your views here.

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
