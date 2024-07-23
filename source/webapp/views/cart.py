from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from webapp.models import CartItem, Product
from webapp.forms import CartItemForm


class AddToCartView(CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'cart/add_to_cart.html'
    success_url = reverse_lazy('products_view')

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        quantity = form.cleaned_data['quantity']
        cart_item = CartItem.objects.filter(product=product).first()
        if cart_item:
            new_quantity = cart_item.quantity + quantity
            if new_quantity <= product.remainder:
                cart_item.quantity = new_quantity
                cart_item.save()
                return HttpResponseRedirect(self.success_url)
            else:
                form.add_error(None, "Недостаточно товара в наличии.")
                return self.form_invalid(form)
        else:
            if quantity <= product.remainder:
                form.instance.product = product
                return super().form_valid(form)
            else:
                form.add_error(None, "Недостаточно товара в наличии.")
                return self.form_invalid(form)


class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart_view.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = context['cart_items']
        total = sum(item.quantity * item.product.price for item in cart_items)
        context['total'] = total
        return context


class RemoveFromCartView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart_view')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
