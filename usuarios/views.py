from django.shortcuts import render
from usuarios.form import LoginForms, CadastroForm

def login(request):
    form = LoginForms()
    return render(request, "usuario/login.html", {"form": form})


def cadastro(request):
    form = CadastroForm()
    return render(request, "usuario/cadastro.html", {"form": form})



