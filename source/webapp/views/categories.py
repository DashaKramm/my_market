from django.db.models import RestrictedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import CategoryForm
from webapp.models import Category


# Create your views here.
def category_add_view(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, "categories/category_add_view.html", context={'form': form})
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_view')
        return render(request, "categories/category_add_view.html", context={'form': form})


def categories_view(request):
    categories = Category.objects.order_by('-id')
    return render(request, 'categories/categories_view.html', context={'categories': categories})


def delete_category(request, *args, pk, **kwargs):
    try:
        get_object_or_404(Category, pk=pk).delete()
    except RestrictedError:
        return render(request, 'categories/categories_view.html',
                      {'error_message': 'Невозможно удалить категорию, так как она используется в товарах'})
    return HttpResponseRedirect(reverse('categories_view'))


def category_edit_view(request, *args, pk, **kwargs):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        form = CategoryForm(instance=category)
        return render(request, "categories/category_edit_view.html", context={'form': form})
    else:
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories_view')
        else:
            return render(request, "categories/category_edit_view.html", context={'form': form})
