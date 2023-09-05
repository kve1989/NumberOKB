FROM python:3-alpine

WORKDIR /app

COPY . .

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt
RUN flask db init && flask db migrate -m "Init migrations" && flask db upgrade

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]