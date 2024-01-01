# # from time import timezone
# #
# # from django.contrib.auth.signals import user_logged_in
# # from django.dispatch import receiver
# #
# # from users.models import User
# #
# #
# # @receiver(user_logged_in, sender=User)
# # def update_last_login(sender=User, user, **kwargs):
# #     User.last_login = timezone.now()
# #     user.save()
# #     print('Hello')
# from django.utils import timezone
# from django.utils.timezone import now
#
# from users.models import User
#
#
# # class SetLastVisitMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response
# #
# #     def __call__(self, request):
# #         response = self.get_response(request)
# #
# #         # Проверяем, что пользователь аутентифицирован и что у него есть токен
# #         if request.user.is_authenticated and hasattr(request, 'auth') and request.auth:
# #             user = request.user
# #             # Обновляем дату последнего входа пользователя
# #             user.last_visit = timezone.now()
# #             user.save()
# #
# #         return response