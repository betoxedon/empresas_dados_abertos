from django.db import models

# Create your models here.


class Empresa(models.Model):
    cnpj = models.CharField(max_length=14)
    natju = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnae_descricao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
