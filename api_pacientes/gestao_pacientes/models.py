from django.db import models

class Paciente(models.Model):
    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo_sanguineo = models.CharField(
        max_length=3,
        choices=TIPO_SANGUINEO_CHOICES
    )

    def __str__(self):
        return f'{self.nome} ({self.tipo_sanguineo})'

class SolicitacaoDoacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #onde será atendido
    hospital = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    #tipo sanguíneo necessário
    tipo_sanguineo_necessario = models.CharField(max_length=3)
    #informações da solicitação
    urgente = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f'Solicitação #{self.id} - {self.paciente.nome}'



