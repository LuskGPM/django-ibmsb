import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User, Fatura

import datetime

user_id = 2
lucasMelo = User.objects.get(pk = user_id)
print(lucasMelo.name)

print('-'*20)

ferreira = User.objects.get(pk = 4)
print(ferreira.name)

print('-'*20)

try:
    user_inexistente = User.objects.get(pk = 999)
    print(user_inexistente.name)
except User.DoesNotExist:
    print('Usuario inexistente')
    