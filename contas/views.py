from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            next_url = request.GET.get('next', 'listar_monitorias')
            return redirect(next_url)
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, verifique seu usuário e senha.')
    else:
        form = AuthenticationForm()
    return render(request, 'contas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def registrar_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        else:
            # adicionar classe 'is-invalid' aos widgets dos campos com erro
            for field_name in form.errors:
                if field_name in form.fields:
                    widget = form.fields[field_name].widget
                    existing = widget.attrs.get('class', '')
                    if 'is-invalid' not in existing:
                        widget.attrs['class'] = (existing + ' is-invalid').strip()
    else:
        form = RegistroForm()
    return render(request, 'contas/registrar.html', {'form': form})
