import os
from django.core.management.base import BaseCommand
from telebot import TeleBot
from users.models import User
from habits.models import Habit

bot = TeleBot(os.getenv("SECRET_KEY"), threaded=False)
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков
        bot.infinity_polling()						# Бесконечный цикл бота

    @bot.message_handler(commands=['start'])
    def start(message):
        # здесь напишите код, который будет отправлять вам информацию
        bot.send_message(message.chat.id, "Приветствую! Для дальнейших уведомлений привычках напишите свой Email'")

    @bot.message_handler(func=lambda message: True)
    def handle_email_input(message):
        chat_id = message.chat.id
        email = message.text

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.chat_id = chat_id
            user.save()

            habit = list(Habit.objects.filter(user=user).values())

            action = ', '.join(i["action"] for i in habit)

            bot.send_message(chat_id,
                            text=f'Ваш Email подтвержден. Теперь вы будете получать уведомления в этот чат.'
                            f'Ваши привычки {action}')
        else:
            bot.send_message(chat_id, text='Такого Email не существует. Проверьте ваш Email.')


