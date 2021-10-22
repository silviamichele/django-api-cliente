from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.contrib.auth.models import User

class ClientesListView(ListView):
	model = Clientes 
	template_name = "clientes_list.html"

def createUser(request):
	if request.POST:
		username = request.POST.get('username')
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')

		if pass2 == pass1:
			user = User(username=username, password=pass1, is_staff=True)
			user.set_password(pass1)
			user.save()

	return render(request, 'clientes/create_user.html')