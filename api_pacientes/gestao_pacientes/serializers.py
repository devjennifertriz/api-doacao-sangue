from rest_framework import serializers
from .models import Paciente, SolicitacaoDoacao    

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class SolicitacaoDoacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SolicitacaoDoacao
        fields = '__all__'