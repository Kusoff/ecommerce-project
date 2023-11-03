from http import HTTPStatus


from django.test import TestCase
from django.urls import reverse

from shop.models import Users
from shop.models import Product


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store Test')
        self.assertTemplateUsed(response, 'shop/home.html')

