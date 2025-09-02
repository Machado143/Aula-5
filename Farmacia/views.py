from django.shortcuts import render

# Create your views here.
def inicio(req):
    nome = 'machado'
    return render(req, 'inicio.html', {
        'variavel': nome
    })