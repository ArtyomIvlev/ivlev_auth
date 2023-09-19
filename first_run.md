Запуск приложения через терминал:
1. установить окружение и питон 3.10.12.  c зависимостями -r requirements

2. файл .env_sample пересохранить в .env и поменять настройки в соответствии с БД

3. настроить БД postgre(пользователь, БД, пароли)

4. произвести миграцию
   alembic revision --autogenerate -m 'Initial'
   alembic upgrade head

5. запустить проект
   python src/main.py


Первый запуск(создаем .env и сеть для проекта, поднимаем контейнеры)

1. `cp .env.example .env`
2. `docker network create app_main`
3. `docker-compose up -d --build`

Миграции
```shell
docker compose exec app alembic revision -m "Name_migration" --autogenerate
```
- Run migrations
```shell
docker compose exec app alembic upgrade head
```