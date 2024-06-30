from django.urls import path

from webapp.views import products_view, product_view, category_add_view, product_add_view, categories_view, \
    delete_category, category_edit_view

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/', products_view, name='products_view'),
    path('products/<int:pk>/', product_view, name='product_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', product_add_view, name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('delete/<int:pk>/', delete_category, name='delete_category'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit_view'),
]
