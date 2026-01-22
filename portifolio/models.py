from django.db import models

class Project (models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.TextField()
    descricao_detalhada = models.TextField()
    thumb_projeto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True, null=True)
    url_git = models.CharField()
    tecnologias = models.CharField() #utilizar separando por vígulas
    data_criacao = models.DateTimeField(auto_now_add=True) #utiliza o horário do momento em que é criado

class Skill (models.Model):
    CATEGORIA_CHOICES = [
    ('linguagem', 'Linguagem'),
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('framework', 'Framework'),
    ('ferramenta', 'Ferramenta'),
    ('banco', 'Banco de Dados'),
    ('outros', 'Outros'),
    ]
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('Avançado', 'Avançado'),
    ]
    skill = models.CharField(max_length=100)
    nivel = models.CharField(choices=NIVEL_CHOICES)
    categoria = models.CharField(choices=CATEGORIA_CHOICES)

class Contato (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField()

class Profile (models.Model):
    nome = models.CharField(max_length=100)
    titulo_profissional = models.CharField(max_length=255)
    bio_curta = models.TextField()
    bio_longa = models.TextField()
    email = models.EmailField()
    link_git = models.CharField()
    link_linkedin = models.CharField()