from django.shortcuts import render

# Create your views here.
from webapp.models import Product


# Create your views here.
def products_view(request):
    products = Product.objects.order_by('-id')
    return render(request, 'products_view.html', context={'products': products})
