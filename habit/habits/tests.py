import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

from habits.models import Habit


class HabitModelTest(APITestCase):

    def setUp(self) -> None:
        pass




    def test_create_habit(self):
        'Тестирование создания урока'
        user = User.objects.create(username='pavel', password='123')
        self.client.force_authenticate(user)
        data = {

            'place': 'Парк',
            'time': '08:00:00',
            'action': 'Утренняя пробежка',
            'is_pleasurable': False,
            'frequency': 'weekly',
            'reward': 'Завтрак с любимыми продуктами',
            'estimated_time': 30,
            'is_public': True,
            'habit_date': '2022-12-31'
        }
        response = self.client.post(
            '/habits/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )



        self.assertTrue(
            Habit.objects.exists()
        )

    def test_list_habit(self):
        user = User.objects.create(username='pavel', password='123')
        self.client.force_authenticate(user)

        Habit.objects.create(
            place = 'Парк',
            time = '08:00:00',
            action = 'Утренняя пробежка',
            is_pleasurable = False,
            frequency = 'weekly',
            reward = 'Завтрак с любимыми продуктами',
            estimated_time = 30,
            is_public = True,
            habit_date = '2022-12-31'
        )

        response = self.client.get(
            '/habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_pk_habit(self):
        user = User.objects.create_user(username='pavel', password='123')
        user.is_superuser = True
        self.client.force_authenticate(user)

        habit = Habit.objects.create(
            user=user,
            place = 'Парк',
            time = '08:00:00',
            action = 'Утренняя пробежка',
            is_pleasurable = False,
            frequency = 'weekly',
            reward = 'Завтрак с любимыми продуктами',
            estimated_time = 30,
            is_public = True,
            habit_date = '2022-12-31'
        )

        response = self.client.get(
            f'/habits/{habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        user = User.objects.create_user(username='pavel', password='123')
        self.client.force_authenticate(user)

        habit = Habit.objects.create(
            user=user,
            place='Парк',
            time='08:00:00',
            action='Утренняя пробежка',
            is_pleasurable=False,
            frequency='weekly',
            reward='Завтрак с любимыми продуктами',
            estimated_time=30,
            is_public=True,
            habit_date='2022-12-31'
        )

        new_place = 'Стадион'
        new_action = 'Ходьба'

        response = self.client.put(
            f'/habits/{habit.id}/',
            {
                'place': new_place,
                'time': '08:00:00',
                'action': new_action,
                'is_pleasurable': False,
                'frequency': 'weekly',
                'reward': 'Завтрак с любимыми продуктами',
                'estimated_time': 30,
                'is_public': True,
                'habit_date': '2022-12-31'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем, что урок был обновлен
        updated_lesson = Habit.objects.get(id=habit.id)
        self.assertEqual(updated_lesson.place, new_place)
        self.assertEqual(updated_lesson.action, new_action)

    def test_delete_habit(self):
        user = User.objects.create_user(username='pavel', password='123')
        self.client.force_authenticate(user)

        habit = Habit.objects.create(
            user=user,
            place='Парк',
            time='08:00:00',
            action='Утренняя пробежка',
            is_pleasurable=False,
            frequency='weekly',
            reward='Завтрак с любимыми продуктами',
            estimated_time=30,
            is_public=True,
            habit_date='2022-12-31'
        )

        response = self.client.delete(
            f'/habits/{habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверяем, что урок был удален
        with self.assertRaises(Habit.DoesNotExist):
            Habit.objects.get(id=habit.id)