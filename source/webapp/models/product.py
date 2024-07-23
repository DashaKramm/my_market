from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=120, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, null=False, blank=False,
                                 verbose_name="Категория", related_name='products')
    added_to = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Стоимость")
    image = models.URLField(null=False, blank=False, verbose_name="Изображение")
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name="Остаток")

    def get_absolute_url(self):
        return reverse('product_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} - {self.price} с"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
