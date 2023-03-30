from django import forms
from .models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['slug']

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