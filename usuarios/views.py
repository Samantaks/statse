from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha!= confirmar_senha:
            return HttpResponse("Senhas não conferem!")

        if len(senha)<6:
            return HttpResponse("Senha muito curta!")
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Usuário já existe!")
        
        user = User.objects.create_user(username=username, password=senha)
        user.save()
        return redirect('usuarios/logar')
