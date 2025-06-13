from django.test import TestCase
from rest_framework.test import APIClient
from .models import Todo, People


class TodoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.people = People.objects.create(name="Тестовый пользователь")
        self.todo = Todo.objects.create(title="Тестовая задача", people=self.people)

    def test_get_todos(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_todo(self):
        data = {
            "title": "Новая задача",
            "description": "Описание",
            "people": self.people.id,
            "completed": True,
        }
        response = self.client.post('/api/todos/', data)
        self.assertEqual(response.status_code, 201)

    def test_update_todo(self):
        data = {"title": "Обновлено", "completed": True}
        response = self.client.patch(f'/api/todos/{self.todo.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['completed'])

    def test_delete_todo(self):
        response = self.client.delete(f'/api/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 204)


class PeopleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.people = People.objects.create(name="Тестовый чел")

    def test_get_people(self):
        response = self.client.get('/api/people/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_people(self):
        data = {"name": "Новый чел"}
        response = self.client.post('/api/people/', data)
        self.assertEqual(response.status_code, 201)

    def test_update_people(self):
        data = {"name": "Обновлено"}
        response = self.client.patch(f'/api/people/{self.people.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_people(self):
        response = self.client.delete(f'/api/people/{self.people.id}/')
        self.assertEqual(response.status_code, 204)
