from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Crud

# Create your tests here.

class CRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'omar',
            email = 'omar@gmail.com',
            password = 'omarzain'
        )
        self.crud = Crud.objects.create(
            name = 'pizza',
            rank = 10,
            eater = self.user
        )

    def test_crud_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_crud_details_status(self):
        response = self.client.get(reverse('crud_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_crud_details_content(self):
        response = self.client.get(reverse('crud_details', args='1'))
        self.assertContains(response, 'pizza')

    def test_crud_update(self):
        response = self.client.post(reverse('crud_update', args='1'), {
            'rank': 8,
        })
        self.assertContains(response, 8)
        self.assertNotContains(response, 17)


class CrudTests(TestCase):
    def test_crud_page_status(self):
        # visit the crud list page
        url = reverse('home')
        '/crud/'
        print(url)
        # get the response
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_not_found(self):
        url = '/crud/hello'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_details_page_template(self):
        url = reverse('crud_details', args='1')
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 404)