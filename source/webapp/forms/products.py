from django import forms
from django.forms import widgets

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', 'remainder']
        widgets = {
            'description': widgets.Textarea(attrs={"cols": 24, "rows": 5}),
        }
