FROM python:3.8-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY Path.ini .

RUN pip install --no-cache-dir -r requirements.txt

COPY templates templates

CMD ["python", "app.py"]
