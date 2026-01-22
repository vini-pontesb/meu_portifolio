from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    home = 'home'
    nome = 'Vinicius Pontes'
    context = {
        'home': home,
        'nome': nome
    }
    return render(request, 'home.html', context)
