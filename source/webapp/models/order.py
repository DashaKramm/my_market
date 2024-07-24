from django.db import models


# Create your models here.
class Order(models.Model):
    username = models.CharField(max_length=80, verbose_name="Имя пользователя")
    telephone = models.CharField(max_length=40, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    products = models.ManyToManyField(
        "webapp.Product",
        related_name="orders",
        verbose_name="Товары",
        blank=True,
        through='webapp.ProductOrder',
        through_fields=("order", "product"),
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
