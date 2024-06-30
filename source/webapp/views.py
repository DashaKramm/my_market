from django.shortcuts import render, get_object_or_404

# Create your views here.
from webapp.models import Product


# Create your views here.
def products_view(request):
    products = Product.objects.order_by('-id')
    return render(request, 'products_view.html', context={'products': products})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", context={"product": product})
