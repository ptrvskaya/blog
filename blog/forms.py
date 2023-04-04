from django import forms
from .models import Post

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserFormRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля'
        }

        error_messages = {
            'username': {
                'unique': 'Пользователь с таким именем уже существует',
                'max_length': 'Имя слишком длинное!'
            }
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['slug', 'author']

        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'topic': 'Тема',
            'content': 'Ваш пост',
            'picture': 'Картинка'
        }

        error_messages = {
            'title': {
                'required': 'Поле не должно быть пустым!',
                'max_length': 'Ваш заголовок слишком длинный!',
                'min_length': 'Ваш заголовок слишком короткий!'
            },

            'description': {
                'required': 'Поле не должно быть пустым!',
                'max_length': 'Ваше описание слишком длинное!',
                'min_length': 'Ваше описание слишком короткое!'
            },

            'content': {
                'required': 'Поле не должно быть пустым!',
            },

            'picture': {
                'required': 'Вы забыли прикрепить картинку!',
            },
        }