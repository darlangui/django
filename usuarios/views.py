from django.shortcuts import render, redirect
from usuarios.form import LoginForms, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha_login'].value()

            usuarios = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuarios is not None:
                auth.login(request, usuarios)
                return redirect('index')
            else:
                return redirect('login')

    return render(request, "usuario/login.html", {"form": form})


def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            senha = form["senha_2"].value()
            email = form["email"].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')



    return render(request, "usuario/cadastro.html", {"form": form})



