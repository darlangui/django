from django.shortcuts import render, get_object_or_404
from galeria.models import Foto


def index(request):
    fotografias = Foto.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": foto})


def buscar(request):
    fotografias = Foto.objects.order_by("data").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})
