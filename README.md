Онлайн интернет магазин использованием Fast Api
   - Модели: Пользователи, Продукты, Корзина
   - Идея проекта: Разработка онлайн интернет магазина где моэно посмотреть все товары, добавить свой товар и собрать корзину для покупки.

Требования к проекту:
- [x] Упаковка проекта в docker compose и запуск через docker compose up без дополнительной настройки
- [x] Прохождение flake8 + mypy в соответствии с конфигурациями проекта
- [x] Кеширование всего, что возможно закешировать через redis
- [x] Orm:  sqlalchemy2.0
- [x] Минимальные данные при разворачивании проекта (фикстуры)
- [x] Валидация входящих данных (pydantic)
- [x] Настройки в env
- [x] Без дублирования кода
- [x] poetry как сборщик пакетов
- [x] Обработка ошибок и соответствующие статусы ответов
- [x] В README.md ожидается увидеть как что работает, чтобы можно было ознакомиться проще с проектов

# Run
  
    git clone https://github.com/https://github.com/Peskovatskow-Ignat/FastAPI_online_shop.git
    
    cd FastAPI_online_shop

    docker compose up --build

# API

## auth
`/registration` - creates new user / returns 409 - conflict if user already exists 

>   curl -X POST http://127.0.0.1:8000/auth/register \
    -H "Content-Type: application/json" \
    -d '{
        "username": "test1",
        "password": "test"
    }' 

`auth/token` - returns jwt token for auth

>   curl -X POST http://127.0.0.1:8000/auth/token \
    -H "Content-Type: application/json" \
    -d '{
        "username": "test1",
        "password": "test"
    }' 

`auth/info` - returns user creds from jwt token

>   curl -X POST http://127.0.0.1:8000/auth/info \
    -H "Authorization: Bearer ACCESS_TOKEN"

## crud

`/user` - returns user info 

>  curl -X 'GET' 'http://127.0.0.1:8000/api/v1/user' \
  -H 'accept: application/json'


`/user` - updates user

>   curl -X 'PUT' 'http://127.0.0.1:8000/api/v1/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "username": "string",
  "password": "string",
  "roll": "byuer"
}'

`/user` - delete user 

>   curl -X 'DELETE' 'http://127.0.0.1:8000/api/v1/user' \
  -H 'accept: */*'


# Docker compose
## App - web
> Container with FastAPI application 

## DB - web_db
> ![Schema](README_source/image.png)

## Redis - redis
> 1. **get_cache_title** - creates redis key in this way:
>    - **{settings.REDIS_SIRIUS_CACHE_PREFIX}:{model}:{model_id}**
>    - **settings.REDIS_SIRIUS_CACHE_PREFIX** - for example db schema name
>    - **model** - db model name
>    - **model_id** - db model id
> 
> 
> 2. **redis_set** - sets data to redis
>
> 
> 3. **redis_get** - gets data from redis
>
> 
> 4. **get_redis** - returns redis object


# .env/.env.example
> BIND_PORT=8000
> BIND_IP=0.0.0.0
>    
>    
>    DB_URL=postgresql+asyncpg://postgres:postgres@web_db:5432/main_db
>    JWT_SECRET_SALT=asdasdasdasdasdasd
>    
>    REDIS_HOST=redis
>    REDIS_PORT=6379
>    REDIS_PASSWORD=
>    
>    REDIS_SIRIUS_CACHE_PREFIX=sirius
