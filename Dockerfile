FROM python:3-alpine

WORKDIR /

ENV PYTHONDONTWRITEBYCODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN pip install --no-cache-dir -r requirements.txt --proxy http://192.168.2.30:3128

CMD ["python run.py"]

EXPOSE 5000