import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estudos.settings")
django.setup()

from core.models import User

def createUser():
    usuario = User(name = "Lucas", email = "teste@teste.com")
    usuario.save()
    
if __name__ == "__main__":
    createUser()
    