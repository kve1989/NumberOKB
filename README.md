# Простая админка для статистики

Используется фреймфорк Flask

Для хранения данных используется sqlite
```bash
python -m venv .env
````

Linux:
```bash
source .env\bin\active
```
Windows:
```cmd
./.env/Scripts/activate
````

```bash
pip install -r requirements.txt
flask db init
flask db migrate -m 'Initial migration.'
flask db upgrade
```

## Ошибки и их решения
`ERROR [flask_migrate] Error: Can't locate revision identified by '35e94e9cecb4'`
```bash
flask db revision --rev-id 35e94e9cecb4
flask db migrate
flask db upgrade
```

`ERROR [flask_migrate] Error: Target database is not up to date.`
```bash
flask db stamp head
flask db migrate
flask db upgrade
```