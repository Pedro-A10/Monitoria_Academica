from django import forms
from .models import Monitoria

class MonitoriaForm(forms.ModelForm):
  class Meta:
    model = Monitoria
    fields = [
      'titulo',
      'descricao',
      'professor',]
