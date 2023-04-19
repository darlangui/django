from django.shortcuts import render, get_object_or_404
from galeria.models import Foto


def index(request):
    fotografias = Foto.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": foto})
