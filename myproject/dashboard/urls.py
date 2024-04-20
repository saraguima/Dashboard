from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicial, name='dashboard'),  #pag inicial
    path('upload/', views.upload_arq, name='upload_arq'),  #pag de upload
    path('login/', views.usuario_login, name='usuario_login'),  #pag de login
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)