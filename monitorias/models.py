from django.db import models
from django.contrib.auth.models import User

class Monitoria(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  professor = models.CharField(max_length=100)
  monitor = models.ForeignKey(User, on_delete=models.CASCADE)
  data = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo

