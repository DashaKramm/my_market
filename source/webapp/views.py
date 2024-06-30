from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from webapp.models import Product, Category


# Create your views here.
def products_view(request):
    products = Product.objects.order_by('-id')
    return render(request, 'products_view.html', context={'products': products})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", context={"product": product})


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add_view.html")
    else:
        name = request.POST.get("name")
        description = request.POST.get("description")
        if not description:
            description = None
        Category.objects.create(
            name=name,
            description=description,
        )
        return redirect('products_view')
