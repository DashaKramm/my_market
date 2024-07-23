from django.db import models


# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, null=False, blank=False,
                                verbose_name="Продукт", related_name='cart_item')
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        db_table = "cart_items"
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
