from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tipo_sanguineo = models.CharField(max_length=3)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
