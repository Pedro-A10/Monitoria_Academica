from django.urls import path
from . import views

urlpatterns = [
  path('', views.listar_monitorias, name='listar_monitorias'),
  path('criar/', views.criar_monitoria, name='criar_monitoria'),
  path('atualizar/<int:id>/', views.atualizar_monitoria, name='atualizar_monitoria'),
  path('deletar/<int:id>/', views.excluir_monitoria, name='deletar_monitoria'),
]
