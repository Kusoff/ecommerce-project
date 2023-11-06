# Use your code
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from shop.models import Product, Category


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertEqual(response, 'shop/home.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'characteristics.json', 'manufacturers.json', 'product_images.json', 'goods.json']

    def test_list(self):
        path = reverse('home')
        response = self.client.get(path)

        products = Product.objects.all()
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))

    def test_list_with_category(self):
        category = Category.objects.first()
        path = reverse('products_by_category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(response.filter(category_id=category.id)),
        )

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'shop/home.html')


