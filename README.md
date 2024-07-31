# Тестовое задание от Farpost

## Задача

Задачей было создать веб-приложение, построенное с использованием Django и Dash для отображения информации о пользователях и журналов событий.

## Функциональные возможности

- Ввод логина пользователя для получения данных.
- Интерактивные таблицы данных с информацией о комментариях пользователя и журналами событий.
- Экспорт данных в CSV.

## Требования

- Python 3.10+
- Django 3.0+
- PostgreSQL (или другая предпочтительная база данных)
- Пакеты Python (перечислены в `requirements.txt`)

## Создание моков данных

### Моки для blogers

python manage.py create_mocks_blogers -tm

### Моки для logs

python manage.py create_mocks_logs -tm

## Схема базы данных

### Приложение blogers

Bloger

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- email: EmailField, UNIQUE.
- login: VARCHAR(50), UNIQUE.

Blog

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- name: VARCHAR(100).
- description: VARCHAR(500).
- owner_id: INTEGER, FOREIGN KEY, ссылается на id в таблице Bloger.

Post

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- header: VARCHAR(200).
- text: VARCHAR(2000).
- author_id: INTEGER, FOREIGN KEY, ссылается на id в таблице Bloger.
- blog_id: INTEGER, FOREIGN KEY, ссылается на id в таблице Blog.

Comment

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- text: VARCHAR(2000).
- author_id: INTEGER, FOREIGN KEY, ссылается на id в таблице Bloger.
- post_id: INTEGER, FOREIGN KEY, ссылается на id в таблице Post.
- Приложение logs

[модели приложения blogers](https://github.com/Dezmound1/FarpostTest/blob/main/viewer/blogers/models.py)


### Приложение logs

EventType

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- name: VARCHAR(50).

SpaceType

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- name: VARCHAR(50).

Logs

- id: INTEGER, PRIMARY KEY, автоинкрементный.
- datetime: DateTimeField, auto_now_add=True.
- user_id: INTEGER.
- space_type_id: INTEGER, FOREIGN KEY, ссылается на id в таблице SpaceType.
- event_type_id: INTEGER, FOREIGN KEY, ссылается на id в таблице EventType.

[модели приложения logs](https://github.com/Dezmound1/FarpostTest/blob/main/viewer/logs/models.py)