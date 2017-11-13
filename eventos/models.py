from django.db import models
from django.contrib.auth.models import User
#from django.contrib.postgres.fields import ArrayField

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome + "(" + self.email + ")"

class Funcionario(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True)
    endereço = models.CharField(max_length=256)
    datadeAdimissao = models.DateTimeField(blank=True, null=True)
    funcao = models.CharField(max_length=256)
    def __str__(self):
        return self.pessoa

class Horarios(models.Model):
    funcionario = models.ForeignKey(Funcionario, null=True, blank=True)
    dataEHoraDeChegada = models.DateTimeField(blank=True, null=True)
    dataEHoraDeSaida = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.funcionario

class Frequencia(models.Model):
    horarios = models.ForeignKey(Horarios, null=True, blank=True)
    frequenciafuncionario = models.CharField(max_length=128)
    def __str__(self):
        return self.Horarios

class justificativas(models.Model):
    frequencias = models.ForeignKey(Frequencia, null=True, blank=True)
    justificativas = models.CharField(max_length=128)
    def __str__(self):
        return self.frequencias
