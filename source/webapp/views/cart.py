from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from webapp.forms.orders import OrderForm
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
            else:
                form.add_error(None, "Недостаточно товара в наличии.")
                return self.form_invalid(form)
        else:
            if quantity <= product.remainder:
                form.instance.product = product
                super().form_valid(form)
                next_url = self.request.GET.get('next', self.success_url)
                return redirect(next_url)
            else:
                form.add_error(None, "Недостаточно товара в наличии.")
                return self.form_invalid(form)
        next_url = self.request.GET.get('next', self.success_url)
        return redirect(next_url)


class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart_view.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = context['cart_items']
        total = sum(item.quantity * item.product.price for item in cart_items)
        context['total'] = total
        context['form'] = OrderForm()
        return context


class RemoveFromCartView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart_view')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, pk=kwargs['pk'])
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        next_url = request.POST.get('next', self.success_url)
        return redirect(next_url)
