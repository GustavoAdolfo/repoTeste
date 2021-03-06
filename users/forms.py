from django import forms
from django.contrib.auth.forms import PasswordChangeForm as PdwChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm
from .models import CustomUser, Perfil
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="Nome")
    last_name = forms.CharField(required=True, label="Sobrenome")
    email = forms.EmailField(required=True, label='Email')
    aceite_termos = forms.BooleanField(
        required=True, label='Aceito os termos de uso')
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = [
            "first_name", "last_name", "email",
            "password1", "password2", "aceite_termos",
        ]

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.aceite_termos = self.cleaned_data["aceite_termos"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        # fields = ['username', 'first_name', 'last_name', 'email']
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        # pylint: disable=line-too-long
        self.fields['password'].help_text = "Click <a href=\"../changepassword/\"> Here</a to reset your Password."  # noqa: E501


class PerfilForm(ModelForm):
    user_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Perfil
        model.estado = "SP"
        fields = ['nome', 'sobrenome', 'celular', 'cep', 'logradouro',
                  'numero', 'complemento', 'bairro', 'cidade', 'estado',
                  'url_foto']


class PasswordChangeForm(PdwChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
