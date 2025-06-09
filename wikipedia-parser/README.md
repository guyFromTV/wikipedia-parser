# 📚 Wikipedia Parser (FastAPI + PostgreSQL + AI)

Асинхронный парсер статей Википедии с генерацией кратких описаний через AI

## 🚀 Возможности

- Рекурсивный парсинг статей (до 5 уровней вложенности)
- Генерация кратких описаний через AI (DeepSeek/ChatGPT)
- Хранение данных в PostgreSQL
- Полностью асинхронная архитектура
- REST API для управления процессом
- Поддержка Docker

## 🛠️ Технологии

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0+
- AsyncPG
- Pydantic
- BeautifulSoup4
- httpx

## 🗂️ Структура проекта

wikipedia_parser/
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── parser.py
│ │ └── summary.py
│ ├── core/
│ │ ├── config.py
│ │ └── dependencies.py
│ ├── services/
│ │ ├── parser.py
│ │ └── ai_client.py
│ ├── repositories/
│ │ ├── article.py
│ │ └── summary.py
│ ├── models/
│ │ ├── article.py
│ │ └── summary.py
│ ├── schemas/
│ │ ├── article.py
│ │ └── summary.py
│ └── db/
│ ├── session.py
│ └── init_db.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md