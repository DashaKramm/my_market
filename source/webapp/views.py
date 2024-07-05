from django.db.models import RestrictedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ProductForm
# Create your views here.
from webapp.models import Product, Category


# Create your views here.
def products_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category__name', 'name')
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
        form = ProductForm()
        return render(request, "product_add_view.html", context={'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
        return render(request, "product_add_view.html", context={'form': form})


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
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "product_delete_view.html", context={"product": product})
    else:
        product.delete()
    return HttpResponseRedirect(reverse('products_view'))


def product_edit_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        # categories = Category.objects.all()
        form = ProductForm(instance=product)
        return render(request, "product_edit_view.html", context={'form': form})
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, "product_edit_view.html", context={'form': form})
