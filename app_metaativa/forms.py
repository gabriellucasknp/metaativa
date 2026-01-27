from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Comunidade


class CadastroUsuarioForm(UserCreationForm):
    """Formulário para cadastro de novo usuário"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditarPerfilForm(forms.ModelForm):
    """Formulário para editar perfil do usuário"""
    class Meta:
        model = Perfil
        fields = ('idade', 'atividades', 'objetivo')
        widgets = {
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'atividades': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CriarComunidadeForm(forms.ModelForm):
    """Formulário para criar nova comunidade"""
    dias = forms.CharField(
        max_length=100,
        help_text="Separe os dias com vírgula. Ex: seg,qua,sex",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Comunidade
        fields = ('nome', 'descricao', 'esporte', 'local', 'dias', 'horario')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'esporte': forms.Select(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
