from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/<int:id_profile>', views.sobre, name='sobre'),
    path('projetos/', views.list_projetos, name='projetos'),
]
