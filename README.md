Этот проект представляет собой систему отправки уведомлений о выполнении привычек пользователям.

## Установка

1. Клонируйте репозиторий на локальную машину:

   
   git clone https://github.com/your_username/email-habit.git
   

2. Перейдите в каталог проекта:

   
   cd email-habit
   

3. Установите зависимости:

   
   pip install -r requirements.txt
   

4. Настройте базу данных и другие настройки в файле settings.py.

## Использование

1. Запустите Celery worker:

   
   celery -A emailhabit worker --loglevel=info
   

2. Запустите приложение Django:

   
   python manage.py runserver
   

3. Периодические задачи будут выполняться автоматически благодаря Celery.
