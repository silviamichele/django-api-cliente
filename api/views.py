# from django.shortcuts import render
from rest_framework import generics
from clientes.models import *
from .serializers import *


class ClientesAPIViews(generics.ListAPIView):
	queryset = Clientes.objects.all()
	serializer_class = ClientesSerializer
