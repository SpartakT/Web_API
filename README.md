# BestChange API

REST API для получения данных по обменникам криптовалюты (BTC → RUB) с BestChange.

## О проекте

Проект предоставляет удобный доступ к данным обменников через REST API с поддержкой фильтров, сортировки и пагинации.

### Основные возможности
- Получение списка обменников с фильтрами
- Сортировка по курсу, резерву, отзывам и названию
- Пагинация
- Поиск по названию
- Получение статистики

## Технологии

- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Pandas**

## Как запустить проект

### 1. Клонирование репозитория
```bash
git clone https://github.com/SpartakT/Web_API.git
cd Web_API
```

### 2. Создание виртуального окружения
```bash
python -m venv .venv
```

3. Активация окружения
```bash
.venv\Scripts\activate
```

4. Установка зависимостей
```bash
pip install -r requirements.txt
```

5. Инициализация базы данных
```bash
python run.py init-db
```

6. Запуск сервера
```bash
python run.py run --reload
```