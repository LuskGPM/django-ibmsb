import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User, Fatura

import datetime

data_nascimento = datetime.date(2003, 7, 3)

sthefany = User.objects.get_or_create(
    name = 'Sthefany',
    email = 'teste6@teste.com',
    ativo = False,
    data_nascimento = data_nascimento,
    cpf = '99988877722'
)

print(sthefany)
