from django.urls import path

from webapp.views import ProductListView, ProductDetailView, CategoryCreateView, CreateProductView, CategoryListView, \
    CategoryDeleteView, CategoryUpdateView, DeleteProductView, UpdateProductView, ProductsByCategoryView, \
    AddToCartView, CartView, RemoveFromCartView, OrderCreateView, OrderSuccessView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_view'),
    path('products/', ProductListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add_view'),
    path('products/add/', CreateProductView.as_view(), name='product_add_view'),
    path('categories/', CategoryListView.as_view(), name='categories_view'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete_category'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit_view'),
    path('products/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('products/<int:pk>/edit/', UpdateProductView.as_view(), name='product_edit_view'),
    path('category/<slug:slug>/', ProductsByCategoryView.as_view(), name='products_by_category_view'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/success/', OrderSuccessView.as_view(), name='order_success'),
]
