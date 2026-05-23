from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# O DefaultRouter gera automaticamente as URLs padronizadas para as ViewSets
router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename='profile')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'contatos', views.ContatoViewSet, basename='contato')

# Todas as rotas geradas pelo router são incluídas na lista de urlpatterns do app
urlpatterns = [
    path('', include(router.urls)),
]