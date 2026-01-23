from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato, Project, Profile, Skill

def home (request):
    home = 'home'
    perfil = Profile.objects.all()
    context = {'perfil': perfil, 'home': home}
    return render(request, 'home.html', context)
