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


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "product_add_view.html", context={"categories": categories})
    else:
        name = request.POST.get("name")
        description = request.POST.get("description")
        category_id = request.POST.get("category_id")
        price = request.POST.get("price")
        image = request.POST.get("image")
        if not description:
            description = None
        product = Product.objects.create(
            name=name,
            description=description,
            category_id=category_id,
            price=price,
            image=image,
        )
        return redirect('product_view', pk=product.pk)
