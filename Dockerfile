FROM python:3.11-slim@sha256:a1f5b6e0c9d4f8e3c7b2a5f9d8c1e4b7a0f3c6e9b2d5a8f1c4e7b0a3d6f9c2

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/app
ENV ENABLE_WEB_INTERFACE=true

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]