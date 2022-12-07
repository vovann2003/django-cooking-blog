from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea
from .models import Profile, Comment, Recipe
from django import forms


class ProfileForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    first_name = forms.CharField(label='Имя', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input', 'required': True}))
    last_name = forms.CharField(label='Фамилия', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input', 'required': True}))
    email = forms.EmailField(label='Электронная почта', required=False, widget=forms.EmailInput(attrs={'class': 'form-input', 'required': False}))
    username = forms.CharField(label='Логин', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    """
    Форма для редактирования данных пользователя
    """

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'username', 'photo')


class RecipeForm(forms.ModelForm):
    """
    Форма для добавления рецептов на сайт
    """

    class Meta:
        model = Recipe
        fields = ('title', 'text', 'heading', 'cooking_time', 'photo', 'serving')


class CommentForm(forms.ModelForm):
    """
    Форма для комментариев
    """

    class Meta:
        model = Comment
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 3})
