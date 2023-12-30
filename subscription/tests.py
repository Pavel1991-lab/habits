# <<<<<<< HEAD
# # from rest_framework import status, response
# # from rest_framework.test import APITestCase
# #
# # from subscription.models import Subscription
# # from users.models import User
# # from course.models import Course
# #
# # class SubscriptionTestCase(APITestCase):
# #
# #     def setUp(self) -> None:
# #         pass
# #
# #     def test_create_subscription(self):
# #         'Тестирование создания подписки'
# #         user = User.objects.create(username='pavel', password='123')
# #         self.client.force_authenticate(user)
# #
# #         Course.objects.create(
# #             title='test',
# #             description='test_1'
# #         )
# #
# #         data = {
# #          "course": 1,
# #          "is_active": "True"
# #         }
# #
# #         response = self.client.post(
# #             '/subscription/',
# #             data=data
# #         )
# #
# #
# #
# #         self.assertEqual(
# #             response.status_code,
# #             status.HTTP_201_CREATED
# #         )
# #
# #
# #         self.assertTrue(
# #              Subscription.objects.exists()
# #         )
# #
# #     def test_list_lesson(self):
# #         user = User.objects.create(username='pavel', password='123')
# #         self.client.force_authenticate(user)
# #
# #         Course.objects.create(
# #             title='test',
# #             description='test_1'
# #         )
# #
# #         response = self.client.get(
# #             '/subscription/'
# #         )
# #
# #
# #         self.assertEqual(
# #             response.status_code,
# #             status.HTTP_200_OK
# #         )
# #
# #     def test_update_subscription(self):
# #         user = User.objects.create_user(username='pavel', password='123')
# #         self.client.force_authenticate(user)
# #
# #         course = Course.objects.create(
# #             title='test',
# #             description='test_1'
# #         )
# #
# #         subscription = Subscription.objects.create(
# #             course=course,
# #             is_active=True
# #         )
# #
# #         new_course = Course.objects.create(title='new course', description='new course description')
# #         is_active = False
# #
# #         response = self.client.put(
# #             f'/subscription/{subscription.id}/',
# #             {
# #                 'course': new_course.id,
# #                 'is_active': is_active
# #             }
# #         )
# #
# #         self.assertEqual(
# #             response.status_code,
# #             status.HTTP_200_OK
# #         )
# #
# #         # Проверяем, что подписка была обновлена
# #         updated_subscription = Subscription.objects.get(id=subscription.id)
# #         self.assertEqual(updated_subscription.course, new_course)
# #         self.assertEqual(updated_subscription.is_active, is_active)
# #
# #     def test_delete_subscription(self):
# #         user = User.objects.create_user(username='pavel', password='123')
# #         self.client.force_authenticate(user)
# #
# #
# #         course = Course.objects.create(
# #             title='test',
# #             description='test_1'
# #         )
# #
# #         subscription = Subscription.objects.create(
# #             course=course,
# #             is_active=True
# #         )
# #
# #
# #         response = self.client.delete(
# #             f'/subscription/{subscription.id}/'
# #         )
# #
# #         self.assertEqual(
# #             response.status_code,
# #             status.HTTP_204_NO_CONTENT
# #         )
# #
# #         # Проверяем, что урок был удален
# #         with self.assertRaises(Subscription.DoesNotExist):
# #             Subscription.objects.get(id=subscription.id)
#
# from rest_framework import status, response
# from rest_framework.test import APITestCase
#
# from subscription.models import Subscription
# from users.models import User
# from course.models import Course
#
# class SubscriptionTestCase(APITestCase):
#
#     def setUp(self) -> None:
#         pass
#
#     def test_create_subscription(self):
#         'Тестирование создания подписки'
#         user = User.objects.create(username='pavel', password='123')
#         self.client.force_authenticate(user)
#
#         Course.objects.create(
#             title='test',
#             description='test_1'
#         )
#
#         data = {
#          "course": 1,
#          "is_active": "True"
#         }
#
#         response = self.client.post(
#             '/subscription/',
#             data=data
#         )
#
#
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#
#         self.assertTrue(
#              Subscription.objects.exists()
#         )
#
#     def test_list_lesson(self):
#         user = User.objects.create(username='pavel', password='123')
#         self.client.force_authenticate(user)
#
#         Course.objects.create(
#             title='test',
#             description='test_1'
#         )
#
#         response = self.client.get(
#             '/subscription/'
#         )
#
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#     def test_update_subscription(self):
#         user = User.objects.create_user(username='pavel', password='123')
#         self.client.force_authenticate(user)
#
#         course = Course.objects.create(
#             title='test',
#             description='test_1'
#         )
#
#         subscription = Subscription.objects.create(
#             course=course,
#             is_active=True
#         )
#
#         new_course = Course.objects.create(title='new course', description='new course description')
#         is_active = False
#
#         response = self.client.put(
#             f'/subscription/{subscription.id}/',
#             {
#                 'course': new_course.id,
#                 'is_active': is_active
#             }
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         # Проверяем, что подписка была обновлена
#         updated_subscription = Subscription.objects.get(id=subscription.id)
#         self.assertEqual(updated_subscription.course, new_course)
#         self.assertEqual(updated_subscription.is_active, is_active)
#
#     def test_delete_subscription(self):
#         user = User.objects.create_user(username='pavel', password='123')
#         self.client.force_authenticate(user)
#
#
#         course = Course.objects.create(
#             title='test',
#             description='test_1'
#         )
#
#         subscription = Subscription.objects.create(
#             course=course,
#             is_active=True
#         )
#
#
#         response = self.client.delete(
#             f'/subscription/{subscription.id}/'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
#
#         # Проверяем, что урок был удален
#         with self.assertRaises(Subscription.DoesNotExist):
#             Subscription.objects.get(id=subscription.id)
#
#
