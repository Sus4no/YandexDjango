from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email',)


class SignUpForm(forms.ModelForm):

    confirm_password = forms.Field(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Повторите пароль')

    class Meta:
        user = get_user_model()

        model = user

        fields = (user.email.field.name,
                  user.password.field.name)
        labels = {
            user.email.field.name: 'Email',
            user.password.field.name: 'Пароль',
        }
        widgets = {
            user.email.field.name: forms.EmailInput(
                attrs={'class': 'form-control'}),
            user.password.field.name: forms.PasswordInput(
                attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Email')
    first_name = forms.Field(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Имя')
    birthday = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        label='День рождения', widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = get_user_model()

        fields = ('first_name',)
