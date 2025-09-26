import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User, Fatura

def createUser(name, email, cpf):
    
    user = User(
        name=name, 
        email=email, 
        cpf=cpf,
        )
    
    fatura = Fatura(
        user=user,
        valor=100.00,
        pago=False
    )
    
    user.save()
    fatura.save()
    
    

if __name__ == "__main__":
    createUser('Maria', 'teste5@teste.com', '44422244455')
    