Запуск приложения через терминал:
1. установить окружение и питон 3.10.12.  c зависимостями -r requirements

2. файл .env_sample пересохранить в .env и поменять настройки в соответствии с БД

3. настроить БД postgre(пользователь, БД, пароли)

4. произвести миграцию
   alembic revision --autogenerate -m 'Initial'
   alembic upgrade head

5. запустить проект
   python src/main.py