import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import Fatura, User

users = User.objects.all()

for user in users:
    print(user.name)
    print(user.email)

faturas = Fatura.objects.all()

for fatura in faturas:
    print(fatura.valor)
    print(f'CPF do cliente = {fatura.user.cpf}')
    