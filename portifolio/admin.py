from django.contrib import admin
from .models import Contato, Profile, Project, Skill


class Projects(admin.ModelAdmin):
    list_display = ['titulo', 'descricao_curta', 'data_criacao']
    search_fields = ['titulo']


class Profiles(admin.ModelAdmin):
    list_display = ['nome', 'bio_curta']

class Skills(admin.ModelAdmin):
    list_display = ['skill', 'nivel', 'categoria']
    search_fields = ['skill']
    list_filter = ['categoria']


admin.site.register(Contato)
admin.site.register(Profile, Profiles)
admin.site.register(Project, Projects)
admin.site.register(Skill, Skills)
