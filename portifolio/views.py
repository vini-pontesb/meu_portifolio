from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contato, Project, Profile, Skill
from .forms import ContatoForm

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

def detalhar_projetos (request, id_projeto):
    projeto = Project.objects.get(id = id_projeto)
    context = {'projeto': projeto} 
    return render(request, 'detalhes_projeto.html', context)

def buscar_projeto (request):
    titulo_buscado = request.GET.get('titulo')
    if titulo_buscado:
        projetos_encontrados = Project.objects.filter(titulo__icontains=titulo_buscado).order_by('titulo')
    else:
        projetos_encontrados = None
    context = {'projetos_encontrados': projetos_encontrados, 'buscar': True}
    return render(request, 'projetos.html', context)

def contato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            email_cliente = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            mensagem_final = f"Novo contato recebido!\n\nNome: {nome}\nE-mail: {email_cliente}\n\nMensagem:\n{mensagem}"
            try:
                send_mail(
                subject=f"Novo contato do site: {assunto}",
                message = mensagem_final,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=['viniciusbragacontatos@gmail.com'],
                fail_silently=False
                )
                messages.success(request, 'Mensagem enviada com sucesso')
            except Exception as e:
                messages.error(request, 'Erro ao enviar email. Mas seus dados foram salvos')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao enviar. Verifique os campos')
    else:
        form = ContatoForm()
    context = {'form': form}
    return render(request, 'contato.html', context)
