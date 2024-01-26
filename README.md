Тестовое задание.  
В тестовом задании используется база данных `sqlite` так как не было написано какую  
конкретно базу данных использовать для хранения данных.  
Для того чтобы запустить приложение достаточно скопировать его с github.  
Далее после того как скачаете проект надо утсановить все зависимости для корректной работы  
нужно выполнить команду `pip install -r requirements.txt`.  
Выполните миграции командой `python manage.py migrate`.  
Далее можно запустить проект командой `python manage.py runserver`.  
Если команды не работают убедитесь что вы находиться в той директории где находятся данные файлы,  
если не находитесь то либо пропишите путь в команде либо перейдите в директорию с файлом.  
Для того чтобы работать из панели администратора нужно для начала создать пользователя  
сделать это можно командой `python manage.py createsuperuser`.  
Далее переходите по адресу `http://127.0.0.1:8000/admin/` и вводите данные созданного пользователя.  
