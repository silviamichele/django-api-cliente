from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ClientesListView.as_view(), name="home"),
    path('create_user/', views.createUser)
]