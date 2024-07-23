from django import forms

from webapp.models import CartItem


class CartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        label="Количество",
        widget=forms.NumberInput(attrs={'placeholder': 'Введите количество'})
    )

    class Meta:
        model = CartItem
        fields = ['quantity']
