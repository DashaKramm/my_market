from django.db.models import RestrictedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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
        Category.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description") or None,
        )
        return redirect('products_view')


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "product_add_view.html", context={"categories": categories})
    else:
        product = Product.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description") or None,
            category_id=request.POST.get("category_id"),
            price=request.POST.get("price"),
            image=request.POST.get("image"),
            remainder=request.POST.get("remainder"),
        )
        return redirect('product_view', pk=product.pk)


def categories_view(request):
    categories = Category.objects.order_by('-id')
    return render(request, 'categories_view.html', context={'categories': categories})


def delete_category(request, *args, pk, **kwargs):
    try:
        get_object_or_404(Category, pk=pk).delete()
    except RestrictedError:
        return render(request, 'categories_view.html',
                      {'error_message': 'Невозможно удалить категорию, так как она используется в товарах'})
    return HttpResponseRedirect(reverse('categories_view'))


def category_edit_view(request, *args, pk, **kwargs):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        return render(request, "category_edit_view.html", {"category": category})
    else:
        category.name = request.POST.get("name")
        category.description = request.POST.get("description") or None
        category.save()
        return redirect('categories_view')


def delete_product(request, *args, pk, **kwargs):
    get_object_or_404(Product, pk=pk).delete()
    return HttpResponseRedirect(reverse('products_view'))


def product_edit_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "product_edit_view.html", {"product": product, "categories": categories})
    else:
        product.name = request.POST.get("name")
        product.description = request.POST.get("description") or None
        product.category_id = request.POST.get("category_id")
        product.price = request.POST.get("price")
        product.image = request.POST.get("image")
        product.remainder = request.POST.get("remainder")
        product.save()
        return redirect('product_view', pk=product.pk)
