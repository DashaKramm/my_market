from django.urls import path

from webapp.views import ProductListView, ProductDetailView, category_add_view, CreateProductView, categories_view, \
    delete_category, category_edit_view, DeleteProductView, UpdateProductView, ProductsByCategoryView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_view'),
    path('products/', ProductListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', CreateProductView.as_view(), name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/delete/', delete_category, name='delete_category'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit_view'),
    path('products/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('products/<int:pk>/edit/', UpdateProductView.as_view(), name='product_edit_view'),
    path('category/<slug:slug>/', ProductsByCategoryView.as_view(), name='products_by_category_view'),
]
