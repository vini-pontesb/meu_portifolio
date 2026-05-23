from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Contato, Project, Profile, Skill
from .serializers import ContatoSerializer, ProjectSerializer, ProfileSerializer, SkillSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    # Mantemos a ordenação original e a otimização de queries das imagens
    queryset = Project.objects.prefetch_related('images').all().order_by('data_criacao')
    serializer_class = ProjectSerializer
    
    # Substitui a antiga view 'buscar_projeto' de forma elegante
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'tecnologias'] # Bônus: Agora busca no título E nas tecnologias

    # Substitui a lógica de separar as tecnologias por vírgula da antiga view 'list_projetos'
    @action(detail=False, methods=['get'])
    def tecnologias(self, request):
        
        # Endpoint extra: /api/projects/tecnologias/ 
        # Retorna um array limpo com todas as tecnologias cadastradas no banco, sem repetições.
        todas_techs_banco = Project.objects.values_list('tecnologias', flat=True)
        tech_set = set()
        for tech_string in todas_techs_banco:
            if tech_string:
                partes = [t.strip() for t in tech_string.split(',')]
                tech_set.update(partes)
        return Response(sorted(list(tech_set)))

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    # Substitui a lógica de envio de formulário da antiga view 'contato'
    def perform_create(self, serializer):
        # Intercepta a criação do Contato.
        # Primeiro salva no banco, depois tenta disparar o e-mail.
  
        # Salva a instância no banco de dados
        contato = serializer.save()
        # Monta e dispara o e-mail
        mensagem_final = f"Novo contato recebido via API!\n\nNome: {contato.nome}\nE-mail: {contato.email}\n\nMensagem:\n{contato.mensagem}"
        
        try:
            send_mail(
                subject=f"Novo contato do portfólio: {contato.assunto}",
                message=mensagem_final,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['viniciusbragacontatos@gmail.com'],
                fail_silently=False
            )
        except Exception as e:
            # Em arquiteturas robustas, o erro de e-mail não deve impedir que a API responda "201 Created"
            # O dado está salvo no banco. Apenas logamos o erro para auditoria.
            print(f"Erro no disparo de e-mail via API: {e}")