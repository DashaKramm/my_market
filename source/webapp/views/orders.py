from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from webapp.forms.orders import OrderForm
from webapp.models import CartItem, ProductOrder, Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'cart/cart_view.html'
    success_url = reverse_lazy('order_success')

    def form_valid(self, form):
        cart_items = CartItem.objects.all()
        if not cart_items.exists():
            return self.form_invalid(form)
        response = super().form_valid(form)
        order = self.object
        for item in cart_items:
            ProductOrder.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            product = item.product
            product.remainder -= item.quantity
            product.save()
        cart_items.delete()
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.all()
        context['total'] = sum(item.quantity * item.product.price for item in context['cart_items'])
        return context


class OrderSuccessView(TemplateView):
    template_name = 'cart/order_success.html'
