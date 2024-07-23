from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование", unique=True)
    description = models.TextField(max_length=120, null=True, blank=True, verbose_name="Описание")
    slug = models.SlugField(null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
