from django.db import models


class ProductOrder(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='orders_products', on_delete=models.CASCADE)
    order = models.ForeignKey('webapp.Order', related_name='products_orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
