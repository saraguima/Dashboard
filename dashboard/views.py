from django.shortcuts import render
from .forms import formularios_upload

def upload_arq(request):
    if request.method == 'POST':
        form = formularios_upload(request.POST, request.FILES)
        

