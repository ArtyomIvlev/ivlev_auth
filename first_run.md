# Docker
## Первый запуск(создаем .env, сеть для проекта и поднимаем контейнеры)

1. `cp .env_sample .env`
2. `docker network create app_main`
3. `docker-compose up -d --build`

- Миграции
```shell
docker compose exec app alembic revision -m "Name_migration" --autogenerate
```
- Run migrations
```shell
docker compose exec app alembic upgrade head
```



## Troubleshooting

- занят порт 5432
```
    sudo lsof -i tcp:5432
    sudo kill PID
```
- права на скрипты
```
    chmod +x ./scripts/start-dev.sh
```

# Запуск приложения через терминал:
1. Установить окружение и питон 3.10.12.  c зависимостями -r requirements

2. Файл .env_sample пересохранить в .env и поменять настройки в соответствии с БД

3. Настроить БД postgre(пользователь, БД, пароли)

4. Произвести миграцию
   alembic revision --autogenerate -m 'Initial'
   alembic upgrade head

5. Запустить проект
    uvicorn src.main:app --log-level debug

    
# Тесты:
1. Создать пустую базу для тестов в соответствии с параметрами из .env
2. Запуск тестов pytest -v
