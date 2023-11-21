# Generated by Django 4.1.7 on 2023-11-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_basket_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(blank=True, default=0, verbose_name='Скидка'),
        ),
        migrations.AddField(
            model_name='product',
            name='first_price',
            field=models.IntegerField(default=0, verbose_name='Первоначальная цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='last_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Конечная  цена'),
        ),
    ]
