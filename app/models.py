from audioop import max

from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    Nome = models.CharField(max_length=150)
    Cargo = models.CharField(max_length=30)
    Nivel = models.CharField(max_length=50)