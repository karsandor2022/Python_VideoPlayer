FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 8000

# Use Gunicorn WSGI server (correct for Flask)
CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:8000", "-w", "4"]