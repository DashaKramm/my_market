from django import forms
from django.forms import widgets

from webapp.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': widgets.Textarea(attrs={"cols": 24, "rows": 5}),
        }
