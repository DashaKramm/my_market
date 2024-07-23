from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ProductSearchForm
from webapp.models import Product, Category


# Create your views here.
class ProductListView(ListView):
    template_name = 'products/products_view.html'
    model = Product
    context_object_name = 'products'
    ordering = ['category__name', 'name']
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return ProductSearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(remainder__gte=1)
        if self.search_value:
            queryset = queryset.filter(name__icontains=self.search_value)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class ProductDetailView(DetailView):
    template_name = "products/product_view.html"
    model = Product

    def get_object(self, queryset=None):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return product


class CreateProductView(CreateView):
    template_name = "products/product_add_view.html"
    form_class = ProductForm


class DeleteProductView(DeleteView):
    template_name = "products/product_delete_view.html"
    model = Product
    success_url = reverse_lazy("products_view")


class UpdateProductView(UpdateView):
    template_name = "products/product_edit_view.html"
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})


class ProductsByCategoryView(ListView):
    template_name = 'products/products_by_category_view.html'
    model = Product
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        self.category = self.get_category()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return ProductSearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_category(self):
        return get_object_or_404(Category, slug=self.kwargs.get('slug'))

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.category, remainder__gte=1)
        if self.search_value:
            queryset = queryset.filter(name__icontains=self.search_value)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        context["category"] = self.category
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context
