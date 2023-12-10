
from datetime import datetime, timedelta
from celery import shared_task

from habits.models import Habit
from users.models import User

from habits.management.commands.bot import bot


@shared_task
def emailhabit():

        current_time = datetime.now().time()
        current_date = datetime.now().date()
        user = User.objects.get(email="sotnikov.pavel.91@mail.ru")
        chat_id = user.chat_id
        user.save()
        all_habit = Habit.objects.all()


        for hab in all_habit:

            if hab.habit_date == current_date and hab.frequency == 'daily':

                action = hab.action
                hab_time = hab.time
                hab_date = hab.habit_date

                bot.send_message(chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time}, {hab_date} числа'
                                      f'Ваша привычка {action}')

                hab.habit_date += timedelta(days=1)
                hab.save()

                break

            elif hab.frequency == 'weekly' and hab.habit_date == current_date:

                action = hab.action
                hab_time = hab.time
                hab_date = hab.habit_date

                bot.send_message(chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time}, {hab_date} числа'
                                      f'Ваша привычка {action}')

                hab.habit_date += timedelta(days=7)
                hab.save()

                break

            elif hab.habit_time <= current_time and hab.frequency == 'each hour':

                action = hab.action
                hab_time = hab.habit_time


                bot.send_message(chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time}, сегодня'
                                      f'Ваша привычка {action}')

                time_str = hab.time.strftime('%H:%M:%S')
                time_obj = datetime.strptime(time_str, '%H:%M:%S')
                new_time_obj = time_obj + timedelta(hours=1)
                new_time_str = new_time_obj.strftime('%H:%M:%S')
                hab.habit_time = new_time_str
                hab.save()

                break





        else:
            bot.send_message(chat_id, text='Такого Email не существует. Проверьте ваш Email.')