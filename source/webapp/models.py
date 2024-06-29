from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование", unique=True)
    description = models.CharField(max_length=70, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, null=False, blank=False,
                                 verbose_name="Категория", related_name='products')
    added_to = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Стоимость")
    image = models.URLField(null=False, blank=False, verbose_name="Изображение")

    def __str__(self):
        return f"{self.pk}) {self.name} - {self.price}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
