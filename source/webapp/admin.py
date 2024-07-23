from django.contrib import admin

# Register your models here.
from webapp.models import Product, Category, CartItem


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'added_to', 'price', 'remainder']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name', 'description', 'category', 'price']
    fields = ['name', 'description', 'category', 'added_to', 'price', 'image', 'remainder']
    readonly_fields = ['added_to']


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    list_display_links = ['id', 'product']
    search_fields = ['product__name']
    fields = ['quantity']


admin.site.register(CartItem, CartAdmin)
