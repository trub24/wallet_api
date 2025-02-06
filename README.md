Это просто API для управления кошельком.

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

https://github.com/trub24/wallet_api.git


Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Примеры.

GET запрос: http://127.0.0.1:8000/api/v1/wallets/{WALLET_UUID}

POST запрос: http://127.0.0.1:8000/api/v1/wallets/<WALLET_UUID>/operation

```
{
operationType: DEPOSIT or WITHDRAW,
amount: 1000
}

```
