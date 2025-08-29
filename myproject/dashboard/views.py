from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
import os

from .forms import UploadFileForm
from .models import Venda

def inicial(request):
    # monta dados simples pro gráfico a partir do Model (se vazio, manda arrays vazios)
    qs = Venda.objects.all().order_by('ano', 'mes')
    mes = [v.mes for v in qs]
    vendas = [float(v.valor_vendas) for v in qs]

    chart_data = json.dumps({"mes": mes, "vendas": vendas})
    return render(request, 'dashboard.html', {"chart_data": chart_data})


def upload_arq(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['files']
            # salva o arquivo em MEDIA_ROOT/uploads/
            upload_dir = os.path.join(getattr(settings, "MEDIA_ROOT", "media"), "uploads")
            os.makedirs(upload_dir, exist_ok=True)
            fs = FileSystemStorage(location=upload_dir)
            fs.save(f.name, f)
            return render(request, 'upload_form.html', {"form": UploadFileForm()})
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})


def usuario