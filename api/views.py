# from django.shortcuts import render
from rest_framework import generics, permissions
from clientes.models import *
from .serializers import *


class ClientesAPIViews(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticated,) 
	queryset = Clientes.objects.all()
	serializer_class = ClientesSerializer
