from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularios_upload
from django.contrib.auth import authenticate, login

def inicial(request):
    return render(request, 'dashboard.html')


def upload_arq(request):
    if request.method == 'POST':
        form = formularios_upload(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # Processar o arquivo aqui
            # Exemplo: salvar o arquivo no servidor
            with open('uploaded_arq.xlsx', 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return render(request, 'upload_form.html')
    else:
        form = formularios_upload()
    return render(request, 'upload_form.html', {'form': form})

def usuario_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'mensagem_erro': 'Usuário ou senha inválidos.'})
    else:
        return render(request, 'login.html')