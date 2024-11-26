FROM python:3.9-slim

WORKDIR /app
COPY add_service.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "add_service.py"]
