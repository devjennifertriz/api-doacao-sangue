from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Doador,CriterioDoacao,DemonstracaoInteresse,LocalDoacao

class DoadorSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Doador
        fields = ['id', 'nome', 'tipo_sanguineo', 'email', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        
        links = {
            "self": reverse('doador-detail', args=[obj.pk], request=request),
            "demonstracoes": reverse('demonstracaointeresse-list', request=request) + f"?doador={obj.pk}",
        }

        user = request.user if request else None
        if user and user.is_authenticated:
            if user.has_perm('api_doadores.change_doador'):
                links['editar'] = reverse('doador-detail', args=[obj.pk], request=request)
            
            if user.has_perm('api_doadores.delete_doador'):
                links['excluir'] = reverse('doador-detail', args=[obj.pk], request=request)

        return links

class CriterioDoacaoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    
    _links = serializers.SerializerMethodField()

    class Meta:
        model = CriterioDoacao
        fields = [
            'id', 
            'titulo', 
            'descricao', 
            'categoria', 
            'categoria_display', 
            '_links'
        ]

    def get__links(self, obj):
        request = self.context.get('request')
        
        links = {
            "self": reverse('criteriodoacao-detail', args=[obj.pk], request=request),
        }


        if obj.saiba_mais:
            links["saiba mais"] = obj.saiba_mais

        
        user = request.user if request else None
        if user and user.is_authenticated:
            if user.has_perm('api_doadores.change_criteriodoacao'):
                links['editar'] = reverse('criteriodoacao-detail', args=[obj.pk], request=request)
            
            if user.has_perm('api_doadores.delete_criteriodoacao'):
                links['excluir'] = reverse('criteriodoacao-detail', args=[obj.pk], request=request)

        return links
class LocalDoacaoSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = LocalDoacao
        fields = ['id', 'nome', 'endereco', 'cidade', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        
        links = {
            "self": reverse('localdoacao-detail', args=[obj.pk], request=request),
        }

        user = request.user if request else None
        if user and user.is_authenticated:
            if user.has_perm('api_doadores.change_localdoacao'):
                links['editar'] = reverse('localdoacao-detail', args=[obj.pk], request=request)

            if user.has_perm('api_doadores.delete_localdoacao'):
                links['excluir'] = reverse('localdoacao-detail', args=[obj.pk], request=request)

        return links
class DemonstracaoInteresseSerializer(serializers.ModelSerializer):
    doador = DoadorSerializer(read_only=True)
    
    doador_id = serializers.PrimaryKeyRelatedField(
        queryset=Doador.objects.all(), source='doador', write_only=True
    )
    
    _links = serializers.SerializerMethodField()

    class Meta:
        model = DemonstracaoInteresse
        fields = [
            'id', 'doador', 'doador_id', 'paciente_id', 
            'data_registro', 'comprovante', '_links'
        ]

    def get__links(self, obj):
        request = self.context.get('request')
        
        links = {
            "self": reverse('demonstracaointeresse-detail', args=[obj.pk], request=request),
            "doador": reverse('doador-detail', args=[obj.doador.pk], request=request),
            "paciente_externo": f"http://localhost:8001/api/pacientes/{obj.paciente_id}/"
        }

        user = request.user if request else None
        if user and user.is_authenticated:
            if user.has_perm('api_doadores.change_demonstracaointeresse'):
                links['editar'] = reverse('demonstracaointeresse-detail', args=[obj.pk], request=request)
            
            if user.has_perm('api_doadores.delete_demonstracaointeresse'):
                links['excluir'] = reverse('demonstracaointeresse-detail', args=[obj.pk], request=request)

        return links
