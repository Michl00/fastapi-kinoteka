# API-FilmCollection (FastAPI + Redis)

Simple REST API app for creating personal film collection, made with **FastAPI** and **Redis** database for permanent data storage.

## **Functions**
* Add films to collection (validation by Pydantic).
* View full colletion.
* Find film by title.
* Delete film from collection.
* Global error handling when database is down.

## **Technologies**
* **Python 3.14**
* **FastAPI** (Uvicorn as ASGI-сервер)
* **Pydantic** (data validation)
* **Redis** (main database in Docker-container)

---

## **Instruction for local deploy**

### 1. Clone repositorie
```bash
git clone https://github.com/Michl00/fastapi-kinoteka.git
cd fastapi-kinoteka
```

### 2. Venv setting
```bash
python -m venv .venv
source .venv/Scripts/activate  # for Windows
pip install -r requirements.txt
```

### 3. Starting Redis database (via Docker)
Make sure that Docker Desktop is up and run:
```bash
docker run --name kinoteka-redis -p 6379:6379 -d redis:latest redis-server --appendonly yes --requirepass "password"
```

### 4. Starting web-server
```bash
uvicorn app.main:app --reload
```
Your app is available at: `http://127.0.0.1:8000`

---

## **Examples of API-endpoints**

| Method | Endpoint | Discription |
| :--- | :--- | :--- |
| **GET** | `/` | Hello message API |
| **GET** | `/catalog/` | Get the entire collection |
| **GET** | `/catalog/{title}` | Find film by title |
| **POST** | `/` | Add new film to collection |
| **DELETE** | `/catalog/del/{title}` | Delete film from database |

> **Interactive documentation:** The entire API specification and convenient panel for testing requests (Swagger UI) can be found at:
`http://127.0.0.1:8000/docs`.

---

# API-Кинотека (FastAPI + Redis)

Простое и быстрое REST API приложение для ведения персонального каталога фильмов, написанное на **FastAPI** с использованием высокопроизводительной базы данных **Redis** в качестве персистентного хранилища.

## **Функционал**
* Добавление фильмов в базу данных (валидация через Pydantic).
* Просмотр всего каталога фильмов.
* Поиск конкретного фильма по его названию.
* Поштучное удаление фильмов из коллекции.
* Глобальная обработка ошибок при отключении базы данных.

## **Стек технологий**
* **Python 3.14**
* **FastAPI** (Uvicorn как ASGI-сервер)
* **Pydantic** (для валидации данных)
* **Redis** (как основная БД в Docker-контейнере)

---

## **Инструкция по локальному развертыванию**

### 1. Клонирование репозитория
```bash
git clone https://github.com/Michl00/fastapi-kinoteka.git
cd fastapi-kinoteka
```

### 2. Настройка виртуального окружения
```bash
python -m venv .venv
source .venv/Scripts/activate  # Для Windows (Git Bash)
pip install -r requirements.txt
```

### 3. Запуск базы данных Redis (через Docker)
Убедитесь, что у вас запущен Docker Desktop, и выполните:
```bash
docker run --name kinoteka-redis -p 6379:6379 -d redis:latest redis-server --appendonly yes --requirepass "password"
```

### 4. Запуск веб-сервера
```bash
uvicorn app.main:app --reload
```
После этого приложение станет доступно по адресу: `http://127.0.0.1:8000`

---

## **Примеры API-эндпоинтов**

| Метод | Эндпоинт | Описание |
| :--- | :--- | :--- |
| **GET** | `/` | Приветственное сообщение API |
| **GET** | `/catalog/` | Получить весь список фильмов |
| **GET** | `/catalog/{title}` | Найти фильм по названию |
| **POST** | `/` | Добавить новый фильм в базу |
| **DELETE** | `/catalog/del/{title}` | Удалить фильм из базы по названию |

> **Интерактивная документация:** Полную спецификацию API и удобную панель для тестирования запросов (Swagger UI) можно найти по адресу `http://127.0.0.1:8000/docs`.
