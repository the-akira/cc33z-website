from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        contato = Contato(nome=nome, email=email, mensagem=mensagem)
        contato.save()
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')  # nome da sua URL
    return render(request,'contato.html')