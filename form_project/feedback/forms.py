from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # exclude = ['rating']# Выбираем поля которые исключим из формы
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }  # Выставляем имена
        error_messages = {
            'name': {
                'max_length': 'Ой как много символов',
                'min_length': 'Ой как мало символов',
                'required': 'Не должно быть пустым'
            },
            'surname': {
                'max_length': 'Ой как много символов',
                'min_length': 'Ой как мало символов',
                'required': 'Не должно быть пустым'
            },
            'feedback': {
                'max_length': 'Ой как много символов',
                'min_length': 'Ой как мало символов',
                'required': 'Не должно быть пустым'
            },
        }
