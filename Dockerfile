FROM python:3.11-slim

WORKDIR /app

# 1. Install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy ALL your files into the container
COPY . .

# 3. Tell Python to look for your files in /app
ENV PYTHONPATH=/app

# Change "app:app" to "Server.app:app"
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]