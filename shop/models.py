from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from sortedm2m.fields import SortedManyToManyField

from ecommerce import settings


# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = AutoSlugField(populate_from='username', unique=True, db_index=True, verbose_name='URL', )
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес', )
    user_photo = models.ImageField(upload_to='user_photo/%Y/%m/%d/', verbose_name='Аватарка', blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = 'Для подтверждения учетной записи для {} перейдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):  # метод который проверяет просрочена ссылка или нет
        return True if now() >= self.expiration else False


class Characteristic(models.Model):
    characteristic_name = models.CharField(max_length=30, verbose_name='Название характеристки')
    value = models.CharField(max_length=20, verbose_name='Значение')

    def __str__(self):
        return f"{self.characteristic_name} {self.value}"

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристи товаров'


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
        return reverse('products_by_category', args=[self.id])

    def __str__(self):
        return self.name


class Product_Images(models.Model):
    img_name = models.CharField(max_length=50, verbose_name='Картинка изображения', blank=True)
    img = models.ImageField(upload_to='img_product/%Y/%m/%d/', verbose_name='Изображение продукта')
    first_img = models.BooleanField(default=False, verbose_name='Главная картинка')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.img_name

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    first_price = models.IntegerField(verbose_name='Первоначальная цена', default=0)
    discount = models.FloatField(verbose_name='Скидка', default=0, blank=True)
    last_price = models.IntegerField(verbose_name='Конечная  цена', blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, null=True, verbose_name='Производитель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    product_photos = SortedManyToManyField(Product_Images, verbose_name='Изображения')
    product_characteristic = SortedManyToManyField(Characteristic, verbose_name='Характеристики')

    class Meta:
        ordering = ('name',)  # упорядочевание категории по имени
        verbose_name = 'product'  # для правильного написания моделей во множественном числе
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.id, self.slug])

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.last_price = int(self.first_price * (1 - self.discount / 100))
        else:
            self.last_price = self.first_price
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.last_price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.last_price),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, product_id, user):
        baskets = Basket.objects.filter(user=user, product_id=product_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_created = False
            return basket, is_created


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100, verbose_name="Наименование производителя", unique=True)
    country = models.CharField(max_length=40, verbose_name='Страна', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )
    photo = models.ImageField(upload_to='img_category/%Y/%m/%d/', verbose_name='Фотография',
                              default='shop/static/img/favicon.svg')

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Discount_For_Product_Category(models.Model):
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория товаров',
                                      blank=True)
    discount_percentage = models.FloatField(verbose_name='Скидка')
    discount_start_date = models.DateField(verbose_name='Начало скидок', auto_now_add=True)
    discount_end_date = models.DateField(verbose_name='Конец скидок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Скидка на категорию продукта'
        verbose_name_plural = 'Скидки на категории продуктов'


class Comments(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Продукты", related_name='comments')
    text = models.TextField(verbose_name="Комментарий", blank=True)
    rating = models.IntegerField(verbose_name='Оценка от 1 до 10 ')
    date = models.DateField(verbose_name='Время', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['rating']
