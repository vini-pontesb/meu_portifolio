from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato, Project, Profile, Skill

def home (request):
    home = 'home'
    context = {'home': home}
    return render(request, 'home.html', context)

def sobre (resquest, id_profile):
    perfil = Profile.objects.get(id = id_profile)
    context = {'perfil': perfil}
    return render(resquest, 'sobre.html', context)

def list_projetos (request):
    projetos = Project.objects.all().order_by('data_criacao')
    context = {'projetos': projetos}
    return render(request, 'projetos.html', context)