from rest_framework import serializers
from clientes.models import *

class ClientesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clientes 
		fields = ('nome', 'sobrenome', 'descricao')