from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Perfil(models.Model):
    """Modelo para armazenar informações de perfil do usuário"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    idade = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(150)])
    atividades = models.CharField(max_length=500, blank=True, help_text="Atividades favoritas")
    objetivo = models.CharField(max_length=500, blank=True, help_text="Objetivo fitness")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    class Meta:
        verbose_name_plural = "Perfis"


class Comunidade(models.Model):
    """Modelo para comunidades de atividades"""
    ESPORTES_CHOICES = [
        ('corrida', 'Corrida'),
        ('yoga', 'Yoga'),
        ('futebol', 'Futebol'),
        ('natacao', 'Natação'),
        ('ciclismo', 'Ciclismo'),
        ('musculacao', 'Musculação'),
        ('danca', 'Dança'),
        ('outro', 'Outro'),
    ]
    
    DIAS_CHOICES = [
        ('seg', 'Segunda'),
        ('ter', 'Terça'),
        ('qua', 'Quarta'),
        ('qui', 'Quinta'),
        ('sex', 'Sexta'),
        ('sab', 'Sábado'),
        ('dom', 'Domingo'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    esporte = models.CharField(max_length=50, choices=ESPORTES_CHOICES)
    local = models.CharField(max_length=300)
    dias = models.CharField(max_length=100, help_text="Ex: seg,qua,sex")
    horario = models.TimeField()
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunidades_criadas')
    membros = models.ManyToManyField(User, related_name='comunidades_membro', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-data_criacao']
        verbose_name_plural = "Comunidades"

    def total_membros(self):
        return self.membros.count() + 1  # +1 para o criador
