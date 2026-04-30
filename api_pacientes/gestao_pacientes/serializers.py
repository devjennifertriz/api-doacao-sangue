from rest_framework import serializers
from .models import Paciente, SolicitacaoDoacao

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'user_id', 'nome', 'telefone', 'foto_perfil', 'tipo_sanguineo']

class SolicitacaoDoacaoSerializer(serializers.ModelSerializer):
    paciente_detalhes = PacienteSerializer(source='paciente', read_only=True)
    
    paciente = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(), write_only=True
    )

    class Meta:
        model = SolicitacaoDoacao
        fields = [
            'id', 'paciente', 'paciente_detalhes', 'hospital', 
            'cidade', 'tipo_sanguineo_necessario', 'urgente', 
            'data_criacao', 'ativa'
        ]