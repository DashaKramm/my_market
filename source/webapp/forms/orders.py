from django import forms
from django.forms import widgets

from webapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'telephone', 'address']
        widgets = {
            'username': widgets.TextInput(attrs={'placeholder': 'Имя'}),
            'address': widgets.TextInput(attrs={'placeholder': 'Адрес'}),
            'telephone': widgets.TextInput(attrs={'placeholder': 'Телефон'}),
        }
