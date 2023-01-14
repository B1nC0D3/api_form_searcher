# API для проверки наличия форм
API для проверки наличия формы. На адрес присылается POST-запрос с данными в теле, и API проверяет есть ли подходящая форма в базе данных.

---
## Запуск приложения
В корневой папке скачанного репозитория выполните:
```
    python3 -m venv venv # use 'python' instead 'python3' for Win
    source venv/bin/activate # source venv/Scripts/activate for Win
    pip3 install -r requirements.txt
    uvicorn main:app  # use 'python' instead 'python3' for Win
```
 API будет доступен по адресу 127.0.0.1. Он имеет единственный route /get_form/. Необходимо отправлять POST-запрос.
 
 Для запуска тестов выполните в корневой папке `pytest`

 ---

## Технологии

- Python 3.9
- FastAPI
- TinyDB
- Pytest