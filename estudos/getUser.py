import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User, Fatura

import datetime

users = User.objects.filter(ativo = True)
for user in users:
    print(user.name, user.email)
print('------------------')

nascimento = datetime.date(2004, 6, 13)
user = User.objects.filter(data_nascimento__gt=nascimento)
for u in user:
    print(u.name, u.data_nascimento)
print('------------------')

user = User.objects.filter(name__in = [
    'Lucas', 'Maria', 'Ferreira'
])
for u in user:
    print(u.name, u.email)