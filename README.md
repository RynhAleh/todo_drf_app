# TODO DRF App

Это простое API-приложение для управления задачами с использованием Django REST Framework.

#### Склонируйте депозиторий:
```bash
git clone https://github.com/RynhAleh/todo_drf_app.git
```
## Установка и запуск
```bash
cd todo_drf_app
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Документация API
Открыть в браузере: <http://127.0.0.1:8000/docs/>

## Тесты
```bash
python manage.py test
```

## Эндпоинты
- `GET /api/todos/` — список задач
- `POST /api/todos/` — создать задачу
- `GET /api/todos/{id}/` — получить задачу
- `PATCH /api/todos/{id}/` — обновить задачу
- `DELETE /api/todos/{id}/` — удалить задачу

- `GET /api/people/` — список пользователей
- `POST /api/people/` — создать пользователя
- `GET /api/people/{id}/` — получить пользователя
- `PATCH /api/people/{id}/` — обновить пользователя
- `DELETE /api/people/{id}/` — удалить пользователя
