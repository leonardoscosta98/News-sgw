from math import fabs
from django.db import models

# Create your models here.

class Sistema(models.Model):
    class Meta:
        verbose_name="Sistema"
        verbose_name_plural="Sistemas"

    nome_sistema     = models.CharField(max_length=255)
    # telefone_suporte = models.CharField(max_length=18, null=True,blank=True)

    def __str__(self) -> str:
        return self.nome_sistema

class Aviso(models.Model):
    class Meta:
        verbose_name="Aviso"
        verbose_name_plural="Avisos"

    descricao = models.CharField(max_length=255)
    imagem_fundo = models.ImageField(verbose_name="imagem de fundo", upload_to="imagens/", null=True, blank=True)   
    data_expiracao = models.DateField(null=True, blank=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descricao
