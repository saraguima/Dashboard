from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicial, name='dashboard'),  #pag inicial
    path('upload/', views.upload_arq, name='upload_arq'),  #pag de upload
    path('login/', views.usuario_login, name='usuario_login'),  #pag de login
]
