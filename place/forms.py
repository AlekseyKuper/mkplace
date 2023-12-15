from django import forms
from .models import Suplier
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class Thingsform(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=2,
        strip=True,
        label='Название'
    )
    description = forms.CharField(
        max_length=50,
        min_length=2,
        strip=True,
        label='Описание',
        widget=forms.Textarea,
        initial="Описание"
    )
    price = forms.IntegerField(
        min_value=1,
        step_size=10,
        label='Стоимость',
        initial=40
    )
    date_expired = forms.DateField(
        label='Срок истечения',
        # widget=forms.SelectDateWidget,
        help_text='Укажите дату истечения срока'
    )
    photo = forms.ImageField(
        label='Фото',
        required=False
    )

class SuplierForm(forms.ModelForm):
    class Meta:
        model = Suplier
        fields = ["title", 'agent_name', "agent_firstname", "agent_patronymic", 'exist']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Название'}),
            'agent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'agent_firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'agent_patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            'exist': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Сотрудничаем?'}),
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Поле не должно начинаться с цифр')
        return title

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': "form-control", }),
    )
    password1 = forms.CharField(
        label='Придумать пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': "form-control", }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'forms-control', }),
        min_length=2,
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

