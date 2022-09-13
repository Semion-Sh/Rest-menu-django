from django import forms
from .models import Review
# class Review(forms.Form):
#     name = forms.CharField(label='Имя', error_messages={
#         'required': 'Введите ваше имя'
#     })
#     surname = forms.CharField(label='Фамилия', error_messages={
#         'required': 'Введите вашу Фамилию'
#     })
#     review = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'col': 20}), label='Отзыв', error_messages={
#         'required': 'Напишите отзыв'
#     })
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'review': 'Отзыв',
            'rating': 'Рейтинг'
        }
        error_messages = {
            'name': {'required': 'Введите ваше имя'},
            'surname': {'required': 'Введите вашу Фамилию'},
            'review': {'required': 'Напишите отзыв'},
            'rating': {'required': 'Напишите отзыв'}
        }





