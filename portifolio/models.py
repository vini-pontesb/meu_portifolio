from django.db import models

class Project (models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.TextField()
    descricao_detalhada = models.TextField()
    thumb_projeto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True, null=True)
    url_git = models.URLField(blank=True, null=True)
    tecnologias = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True) #utiliza o horário do momento em que é criado

    def __str__(self):
        return self.titulo

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fotos_projeto/%d/%m/%Y/')
    nome_pagina = models.CharField(max_length=100)

    def __str__(self):
        return f"Página {self.nome_pagina} do projeto {self.project.titulo}"

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

    def __str__(self):
        return self.skill

class Contato (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Profile (models.Model):
    nome = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    profissao = models.CharField(max_length=255, blank=True, null=True)
    foco = models.CharField(max_length=255, blank=True, null=True)
    stack_tecnologico = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Separe as tecnologias por vírgula. Ex: React, Django, Tailwind"
    )
    titulo_profissional = models.CharField(max_length=255)
    bio_curta = models.TextField()
    bio_longa = models.TextField()
    email = models.EmailField()
    link_git = models.URLField(blank=True, null=True)
    link_linkedin = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.nome
