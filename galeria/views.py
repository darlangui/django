from django.shortcuts import render
from galeria.models import Foto


def index(request):
    fotografias = Foto.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request):
    return render(request, 'galeria/imagem.html')
