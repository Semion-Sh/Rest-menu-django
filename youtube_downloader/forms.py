from django import forms
class Review(forms.Form):
    name = forms.CharField(label='Имя', error_messages={
        'required': 'Введите ваше имя'
    })
    surname = forms.CharField(label='Фамилия', error_messages={
        'required': 'Введите вашу Фамилию'
    })
    review = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'col': 20}), label='Отзыв', error_messages={
        'required': 'Напишите отзыв'
    })
    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


