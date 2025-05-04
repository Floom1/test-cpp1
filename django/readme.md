# Шаблон Django REST API для test-name

Это базовый шаблон Django-проекта для быстрого старта разработки REST API с использованием Django и Django REST Framework.

## Структура проекта

 - api/ - Основное приложение для API
 - core/ - Основные настройки и конфигурации
 - utils/ - Вспомогательные утилиты
 - gitignore - Игнорирование ненужных файлов
 - manage.py - Управление проектом Django
 - requirements.txt - Зависимости проекта

## Установка

1. **Клонируйте репозиторий** (или распакуйте шаблон).

2. **Создайте и активируйте виртуальное окружение**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # В Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте окружение**:

   - Создайте файл `.env` в корне проекта для хранения конфиденциальных данных (например, `SECRET_KEY`, настройки базы данных).
   - Пример `.env`:
     ```
     SECRET_KEY=your-secret-key
     DATABASE_URL=postgres://user:password@localhost:5432/dbname
     DEBUG=True
     ```

5. **Примените миграции**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Создайте суперпользователя** (для доступа к админ-панели):

   ```bash
   python manage.py createsuperuser
   ```

## Запуск

Запустите сервер разработки:

```bash
python manage.py runserver
```

- API будет доступно по адресу: `http://127.0.0.1:8000/api/v1/`
- Админ-панель: `http://127.0.0.1:8000/admin/`

## Использование

- **Добавление эндпоинтов**: Модифицируйте файлы `api/v1/endpoint/views.py` и `api/v1/endpoint/urls.py` для создания новых API-эндпоинтов.
- **Модели**: Определите модели в `api/v1/endpoint/models.py` и примените миграции.
- **Тесты**: Добавляйте тесты в `api/v1/endpoint/tests.py`.
- **Утилиты**: Используйте `api/v1/utils/` для общих функций и классов.

## Зависимости

Зависимости перечислены в `requirements.txt`:

- `Django==3.2.7`: Основной фреймворк.
- `djangorestframework==3.12.4`: Для создания REST API.
- `psycopg2-binary==2.9.2`: Драйвер для PostgreSQL.
- `python-dotenv`: Для работы с `.env`.
- `pre-commit` (dev): Для проверки кода перед коммитами.

## Настройка

- **Добавление новых приложений**:
  1. Создайте новое приложение: `python manage.py startapp new_app`.
  2. Добавьте его в `INSTALLED_APPS` в `api/v1/core/settings.py`.
- **Настройка базы данных**: Убедитесь, что PostgreSQL установлен и настроен, или измените `DATABASES` в `settings.py` для другой базы данных.
- **Кастомизация**: Настройте `api/v1/core/settings.py` для добавления middleware, CORS, аутентификации и т.д.

## Пример .env

```
SECRET_KEY = 'django-insecure-.....'
DEBUG='True'
ALLOWED_HOSTS='127.0.0.1'
```

---
made by [**Floom**](https://github.com/Floom1)