from django.test import TestCase
from rest_framework.test import APIClient

from .models import Student


class StudentAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_students_list_endpoint_returns_200(self):
        Student.objects.create(name='Alice', age=22, city='Lahore')

        response = self.client.get('/api/students/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Alice')
