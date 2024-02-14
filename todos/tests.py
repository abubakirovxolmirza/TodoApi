from django.test import TestCase
from rest_framework.test import APIClient

from .models import Todo
from django.utils import timezone


class TodoTest(TestCase):
    def setUp(self):
        Todo.objects.create(
            title='Python',
            description='Learning python.',
            is_completed=False
        )
        Todo.objects.create(
            title='C++',
            description='Learning C++.',
            is_completed=True
        )

    def test_title(self):
        obj1 = Todo.objects.get(title='Python')
        obj2 = Todo.objects.get(description='Learning C++.')

        self.assertEqual(obj1.title, 'Python')
        self.assertEqual(obj2.title, 'C++')

    def test_description(self):
        obj1 = Todo.objects.get(title='Python')
        obj2 = Todo.objects.get(title='C++')

        self.assertEqual(obj1.description, 'Learning python.')
        self.assertEqual(obj2.description, 'Learning C++.')

    def test_data(self):
        obj1 = Todo.objects.get(title='Python')
        obj2 = Todo.objects.get(title='C++')

        self.assertIsNotNone(obj1.data)
        self.assertIsNotNone(obj2.data)

    def test_is_completed(self):
        obj1 = Todo.objects.get(title='Python')
        obj2 = Todo.objects.get(title='C++')

        self.assertFalse(obj1.is_completed)
        self.assertTrue(obj2.is_completed)


class TodoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        Todo.objects.create(title='Python', data=timezone.now())
        Todo.objects.create(title='C++', data=timezone.now())

    def test_title(self):
        response = self.client.get('/api/')

    def test_status_codes(self):

        response = self.client.get('/apis/')

        self.assertEqual(response.status_code, 404)
