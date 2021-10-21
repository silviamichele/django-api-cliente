# from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class ClientesListView(ListView):
	model = Clientes 
	template_name = "clientes_list.html"

