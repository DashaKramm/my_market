from django import forms


class ProductSearchForm(forms.Form):
    search = forms.CharField(label='Поиск', max_length=50, required=False)
