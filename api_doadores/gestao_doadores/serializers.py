from rest_framework import serializers
from .models import Doador, CriterioDoacao, RegistrarDoacao

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        
        fields = [
            'id', 'user_id', 'nome', 'email', 'data_nascimento', 
            'telefone', 'foto_perfil', 'tipo_sanguineo'
        ]

class CriterioDoacaoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)

    class Meta:
        model = CriterioDoacao
        fields = ['id', 'titulo', 'descricao', 'categoria', 'categoria_display', 'saiba_mais']


class RegistrarDoacaoSerializer(serializers.ModelSerializer):
    doador_detalhes = DoadorSerializer(source='doador', read_only=True)
    
    doador = serializers.PrimaryKeyRelatedField(queryset=Doador.objects.all(), write_only=True)

    class Meta:
        model = RegistrarDoacao
        fields = [
            'id', 'doador', 'doador_detalhes', 'solicitacao_id', 
            'data_registro', 'comprovante'
        ]