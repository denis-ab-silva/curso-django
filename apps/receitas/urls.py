from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('busca', busca, name='buscar'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('deleta_receita/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita_receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita')
]