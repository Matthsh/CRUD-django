from django.contrib import admin
from .models import Pessoa

admin.site.register(Pessoa)

# Usar o comando "python manage.py makemigrations" para criar a pasta migrations
# Usar o comando "python manage.py migrate" para registrar as novas tabelas no banco
