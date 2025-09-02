from datetime import datetime
import re
from django.shortcuts import render

# Create your views here.
def inicio(req):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(req, 'inicio.html', {
        'variavel': lista
    })

def verDataHora(req):
    agora = datetime.now()
    return render(req, 'data-hora.html', {
        'datahora_atual': agora
    
    
    
    })