from django.db import models
from datetime import datetime
class Foto(models.Model):

    opcao_categoria = [
        ("NUBULOSA", "nubulosa"),
        ("ESTRELA", "estrela"),
        ("GALAXIA", "galaxia"),
        ("PLANETA", "planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcao_categoria, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia nome={self.nome}]"

