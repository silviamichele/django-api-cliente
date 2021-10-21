from django.contrib import admin
from django.urls import path, include
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ClientesAPIViews.as_view()),
    path('clientes/', include('clientes.urls')),
]
