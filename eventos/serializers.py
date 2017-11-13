from rest_framework import routers, serializers, viewsets
from eventos.models import *

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('nome', 'email')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('pessoa','endereco', 'datadeAdimissao', 'funcao')

class HorariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horarios
        fields = ('funcionario','dataEHoraDeChegada', 'dataEHoraDeSaida')

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frequencia
        fields = ('horarios','frequenciafuncionario')

class justificativasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = justificativas
        fields = ('frequencias','justificativas')
