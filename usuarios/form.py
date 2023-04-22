from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Cadastro", required=True, max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ex: Joao Silva"
        }))

    senha_login = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Digite sua senha"
        }))


class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(label="Nome de Cadastro", required=True, max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ex: Joao Silva"
        }))

    email = forms.CharField(label="Email de Cadastro", required=True, max_length=100, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ex: seuemail@email.com"
        }))

    senha_1 = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Digite sua senha"
        }))

    senha_2 = forms.CharField(label="Confirme sua Senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Digite sua senha novamente"
        }))


