from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Monitoria
from .forms import MonitoriaForm
from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
  return user_passes_test(lambda u: u.is_staff)(view_func)

@login_required
def listar_monitorias(request):
  monitorias = Monitoria.objects.all()
  return render(request, 'monitorias/listar.html', {'monitorias': monitorias})


@login_required
@admin_required
def criar_monitoria(request):
  if request.method == 'POST':
    form = MonitoriaForm(request.POST)
    if form.is_valid():
      monitoria = form.save(commit=False)
      monitoria.monitor = request.user
      monitoria.save()
      messages.success(request, 'Monitoria criada com sucesso.')
      return redirect('listar_monitorias')
  else:
    form = MonitoriaForm()
  return render(request, 'monitorias/form.html', {'form': form})


@login_required
@admin_required
def atualizar_monitoria(request, id):
  monitoria = get_object_or_404(Monitoria, id=id)
  if request.method == 'POST':
    form = MonitoriaForm(request.POST, instance=monitoria)
    if form.is_valid():
      form.save()
      messages.success(request, 'Monitoria atualizada com sucesso.')
      return redirect('listar_monitorias')
  else:
    form = MonitoriaForm(instance=monitoria)
  return render(request, 'monitorias/form.html', {'form': form})


@login_required
@admin_required
def excluir_monitoria(request, id):
  monitoria = get_object_or_404(Monitoria, id=id)
  if request.method == 'POST':
    monitoria.delete()
    messages.success(request, 'Monitoria excluída com sucesso.')
    return redirect('listar_monitorias')
  return render(request, 'monitorias/deletar.html', {'monitoria': monitoria})
