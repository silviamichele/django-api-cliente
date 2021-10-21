from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ClientesListView.as_view(), name="home"),
]