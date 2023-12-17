from rest_framework import status, response
from rest_framework.test import APITestCase

from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        'Тестирование создания урока'
        user = User.objects.create(username='pavel', password='123')
        self.client.force_authenticate(user)
        data = {
            'title': 'Test',
            'description': 'Test_1'
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )



        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertDictEqual(response.json(), {'id': 1, 'title': 'Test', 'description': 'Test_1', 'photo': None, 'video_link': None, 'course': None, 'user': 1}
)

        self.assertTrue(
             Lesson.objects.exists()
        )

    def test_list_lesson(self):
        user = User.objects.create(username='pavel', password='123')
        self.client.force_authenticate(user)

        Lesson.objects.create(
            title = 'test',
            description = 'test_1'
        )

        response = self.client.get(
            '/lesson/'
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_get_pk_lesson(self):
        user = User.objects.create_user(username='pavel', password='123')
        self.client.force_authenticate(user)

        lesson = Lesson.objects.create(
            title='test_pk',
            description='test_pk'
        )

        response = self.client.get(
            f'/lesson/{lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        user = User.objects.create_user(username='pavel', password='123')
        self.client.force_authenticate(user)

        lesson = Lesson.objects.create(
            title='test_pk',
            description='test_pk'
        )

        new_title = 'updated_title'
        new_description = 'updated_description'

        response = self.client.put(
            f'/lesson/update/{lesson.id}/',
            {
                'title': new_title,
                'description': new_description
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем, что урок был обновлен
        updated_lesson = Lesson.objects.get(id=lesson.id)
        self.assertEqual(updated_lesson.title, new_title)
        self.assertEqual(updated_lesson.description, new_description)

    def test_delete_lesson(self):
        user = User.objects.create_user(username='pavel', password='123')
        self.client.force_authenticate(user)

        lesson = Lesson.objects.create(
            title='test_pk',
            description='test_pk'
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверяем, что урок был удален
        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(id=lesson.id)


