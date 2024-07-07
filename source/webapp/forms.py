from django import forms
from django.forms import widgets

from webapp.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'description': widgets.Textarea(attrs={"cols": 24, "rows": 5}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', 'remainder']
        widgets = {
            'description': widgets.Textarea(attrs={"cols": 24, "rows": 5}),
        }


class ProductSearchForm(forms.Form):
    search = forms.CharField(label='Поиск', max_length=50)
