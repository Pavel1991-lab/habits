from rest_framework import status
from rest_framework.test import APITestCase


class LessonTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_lesson(self):
        'Тестирование создания урока'
        data = {
            'title': 'Test',
            'description': 'Test_1'
        }
        responce = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )