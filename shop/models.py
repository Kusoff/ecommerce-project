from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = AutoSlugField(populate_from='username', unique=True, db_index=True, verbose_name='URL', )
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    mailing_list = models.BooleanField(default=False, blank=True, verbose_name='Рассылка')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес', )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)  # упорядочевание категории по имени
        verbose_name = 'category'  # для правильного написания моделей во множественном числе
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)  # упорядочевание категории по имени
        verbose_name = 'product'  # для правильного написания моделей во множественном числе
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        db_table = 'Cart'

        def __srt__(self):
            return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
