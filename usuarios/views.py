from django.shortcuts import render, redirect
from usuarios.form import LoginForms, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


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
                messages.success(request, f'{nome} logado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

    return render(request, "usuario/login.html", {"form": form})


def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            senha = form["senha_2"].value()
            email = form["email"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'usuario já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
    return render(request, "usuario/cadastro.html", {"form": form})



