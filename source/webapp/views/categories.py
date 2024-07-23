from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.forms import CategoryForm
from webapp.models import Category


# Create your views here.
class CategoryCreateView(CreateView):
    template_name = 'categories/category_add_view.html'
    form_class = CategoryForm
    success_url = reverse_lazy('products_view')


class CategoryListView(ListView):
    template_name = 'categories/categories_view.html'
    model = Category
    context_object_name = 'categories'
    ordering = ['-id']


class CategoryDeleteView(DeleteView):
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("categories_view")


class CategoryUpdateView(UpdateView):
    template_name = 'categories/category_edit_view.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('categories_view')
