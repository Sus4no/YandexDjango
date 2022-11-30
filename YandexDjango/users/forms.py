from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


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
        model = get_user_model()

        fields = (get_user_model().email.field.name,
                  get_user_model().password.field.name)
        labels = {
            get_user_model().email.field.name: 'Email',
            get_user_model().password.field.name: 'Пароль',
        }
        widgets = {
            get_user_model().email.field.name: forms.EmailInput(
                attrs={'class': 'form-control'}),
            get_user_model().password.field.name: forms.PasswordInput(
                attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Email')
    first_name = forms.Field(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Имя')
    birthday = forms.Field(widget=forms.DateInput(
        attrs={'class': 'form-control'}, format='%d.%m.%y'),
        label='День рождения',)

    class Meta:
        model = get_user_model()

        fields = ('first_name',)
