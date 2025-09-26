import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User, Fatura

def createUser():
    import datetime
    
    data_nasc = datetime.date(2005, 6, 13)
    
    user = User(
        name='Lucas Melo', 
        email='teste2@teste.com', 
        cpf='12345678911', 
        data_nascimento=data_nasc
        )
    
    fatura = Fatura(
        user=user,
        valor=100.00,
        pago=False
    )
    
    user.save()
    fatura.save()
    
    

if __name__ == "__main__":
    createUser()
    