# Простая админка для статистики

Используется фреймфорк Flask

Для хранения данных используется sqlite
```
python -m venv venv
````

Linux:
```bash
source venv\bin\active
```
Windows:
```cmd
./venv/Scripts/activate
````

```console
pip install -r requirements.txt
flask db init
flask db migrate -m 'First migrate'
```