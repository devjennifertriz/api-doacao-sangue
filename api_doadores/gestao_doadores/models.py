from django.db import models

class Doador(models.Model):
    user_id = models.IntegerField(unique=True, help_text="ID do usuário no Gateway")
    
    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    foto_perfil = models.ImageField(upload_to='perfil_doadores/', null=True, blank=True)
    
    tipo_sanguineo = models.CharField(
        max_length=3, 
        choices=TIPO_SANGUINEO_CHOICES,
        verbose_name="Tipo Sanguíneo"
    )

    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"

    def __str__(self):
        return f"{self.nome} ({self.tipo_sanguineo})"

class CriterioDoacao(models.Model):
    CATEGORIA_CHOICES = [
        ('REQ', 'Requisito Básico'),
        ('IMP_TEMP', 'Impedimento temporário'),
        ('IMP_DEF', 'Impedimento definitivo')
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length = 10,
        choices = CATEGORIA_CHOICES,
        default = 'REQ'
    )

    saiba_mais = models.TextField(
        blank=True, 
        null=True, 
        help_text="Informações detalhadas sobre este critério."
    )

    class Meta:
        verbose_name = "Critério de Doação"
        verbose_name_plural = "Critérios de Doação"

    def __str__(self):
        return f'{self.get_categoria_display()}: {self.titulo}'

class LocalDoacao(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Local de Doação"
        verbose_name_plural = "Locais de Doação"
    
    def __str__(self):
        return f'{self.nome} - {self.cidade} - {self.endereco}'
    

class DemonstracaoInteresse(models.Model):
    doador = models.ForeignKey(
        'Doador', 
        on_delete=models.CASCADE, 
        related_name="interesses"
    )
    
    solicitacao_id = models.IntegerField(verbose_name="ID da Solicitação Externa")
    
    data_registro = models.DateTimeField(auto_now_add=True)
    
    comprovante = models.FileField(
        upload_to='comprovantes/%Y/%m/', 
        null=True, 
        blank=True,
        help_text="Upload do documento ou exame comprobatório"
    )
    

    class Meta:
        verbose_name = "Demonstração de Interesse"
        verbose_name_plural = "Demonstrações de Interesse"

    def __str__(self):
        return f"Interesse: {self.doador.nome} -> Paciente #{self.paciente_id}"

