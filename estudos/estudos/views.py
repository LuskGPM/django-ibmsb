from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo!")

def idadeFutura(request, idade:int, anoFuturo:int):
    import datetime as dt
    
    ano_atual = dt.datetime.now().year
    idadeFutura = (anoFuturo - ano_atual) + idade
    
    return HttpResponse(f"Em {anoFuturo} você terá {idadeFutura} anos.")
