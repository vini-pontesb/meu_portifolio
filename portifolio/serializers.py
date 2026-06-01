from rest_framework import serializers
from .models import Project, ProjectImage, Skill, Contato, Profile

class ProfileSerializer(serializers.ModelSerializer):
    stack_array = serializers.SerializerMethodField()
   
    class Meta:
        model = Profile
        fields = '__all__'
    
    def get_stack_array(self, obj):
        if obj.stack_tecnologico:
            return [tech.strip() for tech in obj.stack_tecnologico.split(',')]
        return []

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        # Não precisamos retornar o ID do projeto aqui dentro, pois já estará aninhado nele
        fields = ['id', 'image', 'nome_pagina']

class ProjectSerializer(serializers.ModelSerializer):
    # 1. Nested Serializer: Traz as imagens vinculadas ao projeto (usa o related_name='images' definido no seu model)
    images = ProjectImageSerializer(many=True, read_only=True)
    
    # 2. Transformação: Cria um novo campo "tecnologias_array" que não existe no banco, apenas no JSON
    tecnologias_array = serializers.SerializerMethodField()

    class Meta:
        model = Project
        # Listamos explicitamente os campos para incluir os novos campos customizados
        fields = [
            'id', 'titulo', 'descricao_curta', 'descricao_detalhada', 
            'thumb_projeto', 'url_git', 'tecnologias', 'tecnologias_array', 
            'data_criacao', 'images'
        ]

    def get_tecnologias_array(self, obj):
        #Pega a string 'React, Tailwind, Django' e transforma em ['React', 'Tailwind', 'Django']
        if obj.tecnologias:
            # Separa por vírgula e remove espaços vazios nas bordas
            return [tech.strip() for tech in obj.tecnologias.split(',') if tech.strip()]
        return []