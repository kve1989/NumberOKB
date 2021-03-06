FROM python:3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYCODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN python -m pip install --upgrade pip --proxy http://192.168.2.30:3128
RUN python -m pip install -r requirements.txt --proxy http://192.168.2.30:3128
RUN python create_db.py

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]