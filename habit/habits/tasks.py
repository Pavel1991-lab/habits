
from datetime import datetime, timedelta
from celery import shared_task

from habits.models import Habit


from habits.management.commands.bot import bot


@shared_task
def emailhabit():

        current_time = datetime.now().time()
        current_date = datetime.now().date()
        all_habit = Habit.objects.all()


        for hab in all_habit:

            if hab.habit_date == current_date and hab.frequency == 'daily':

                action = hab.action
                hab_time = hab.time
                hab_date = hab.habit_date

                bot.send_message(hab.user.chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time}, {hab_date} числа'
                                      f'Ваша привычка {action}')

                print(hab.user.chat_id)
                hab.habit_date += timedelta(days=1)
                hab.save()



            elif hab.frequency == 'weekly' and hab.habit_date == current_date:

                action = hab.action
                hab_time = hab.time
                hab_date = hab.habit_date

                bot.send_message(hab.user.chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time}, {hab_date} числа'
                                      f'Ваша привычка {action}')

                hab.habit_date += timedelta(days=7)
                hab.save()



            elif hab.time <= current_time and hab.frequency == 'each hour':

                action = hab.action
                hab_time = hab.time


                bot.send_message(hab.user.chat_id,
                                 text=f'Вам нужно выполнить привычку в {hab_time},'
                                      f'сегодня Ваша привычка {action}')

                time_str = hab.time.strftime('%H:%M:%S')
                time_obj = datetime.strptime(time_str, '%H:%M:%S')
                new_time_obj = time_obj + timedelta(hours=1)
                new_time_str = new_time_obj.strftime('%H:%M:%S')
                hab.time = new_time_str
                hab.save()







