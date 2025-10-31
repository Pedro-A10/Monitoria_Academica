from django.shortcuts import render, redirect, get_object_or_404
from monitorias.models import Monitoria
from .forms import MonitoriaForm

def listar_monitorias(request):
    monitorias = Monitoria.objects.all()
    return render(request, 'monitorias/listar.html', {'monitorias': monitorias})

def criar_monitoria(request):
  if request.method == 'POST':
    form = MonitoriaForm(request.POST)
    if form.is_valid():
      monitoria = form.save(commit=False)
      monitoria.monitor = request.user
      monitoria.save()
      return redirect('listar_monitorias')
  else:
      form = MonitoriaForm()
      return render(request, 'monitorias/form.html', {'form': form})

def atualizar_monitoria(request):
  monitoria = get_object_or_404(Monitoria, id=id)
  form = MonitoriaForm(request.POST or None, instance=monitoria)
  if form.is_valid():
    form.save()
    return redirect('listar_monitorias')
  return render(request, 'monitorias/form.html', {'form': form})

def excluir_monitoria(request):
  monitoria = get_object_or_404(Monitoria, id=id)
  if request.method == 'POST':
    monitoria.delete()
    return redirect('listar_monitorias')
  return render(request, 'monitorias/deletar.html', {'form': MonitoriaForm()})
