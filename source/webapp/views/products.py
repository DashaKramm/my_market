from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ProductForm, ProductSearchForm
from webapp.models import Product, Category


# Create your views here.
def products_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category__name', 'name')
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(name=search, remainder__gte=1).order_by('category__name', 'name')
    search_form = ProductSearchForm(initial={'search': search})
    return render(request, 'products/products_view.html', context={'products': products, 'search_form': search_form})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_view.html", context={"product": product})


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "products/product_add_view.html", context={'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
        return render(request, "products/product_add_view.html", context={'form': form})


def delete_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "products/product_delete_view.html", context={"product": product})
    else:
        product.delete()
    return HttpResponseRedirect(reverse('products_view'))


def product_edit_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "products/product_edit_view.html", context={'form': form})
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, "products/product_edit_view.html", context={'form': form})


def products_by_category_view(request, *args, slug, **kwargs):
    category = get_object_or_404(Category, slug=slug)
    search = request.GET.get('search')
    products = Product.objects.filter(category=category, remainder__gte=1).order_by('name')
    if search:
        products = products.filter(name=search)
    search_form = ProductSearchForm(initial={'search': search})
    return render(request, 'products/products_by_category_view.html',
                  context={'products': products, 'category': category, 'search_form': search_form})
