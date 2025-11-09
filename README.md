# Sistema de Monitoria Acadêmica

Projeto Django minimal para gerenciar monitorias.

Setup rápido (Linux / macOS):

1. Criar e ativar um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Aplicar migrações e criar superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Rodar servidor de desenvolvimento:

```bash
python manage.py runserver
```

5. Acessar a aplicação em http://127.0.0.1:8000/ e o admin em http://127.0.0.1:8000/admin/

Observações:
- O tema claro/escuro e o botão de logout já foram adicionados ao `core/base.html`.
- Para desenvolvimento é recomendável usar o ambiente virtual `.venv` criado no passo 1.
