from django.shortcuts import render
from eventos.models import *
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from eventos.serializers import *

class PessoaViewSet (viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class FuncionarioViewSet (viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class HorariosViewSet (viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer

class FrequenciaViewSet (viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class justificativasViewSet (viewsets.ModelViewSet):
    queryset = justificativas.objects.all()
    serializer_class = justificativasSerializer
# Create your views here.
