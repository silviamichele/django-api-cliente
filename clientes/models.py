from django.db import models

# Create your models here.
class Clientes(models.Model):
	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50)
	descricao = models.TextField(max_length=255)

	def __str__(self):
		return f'{self.sobrenome.upper()}, {self.nome}'