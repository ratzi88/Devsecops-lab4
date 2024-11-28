FROM python:3.9-slim

WORKDIR /app
COPY status_service.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "status_service.py"]
