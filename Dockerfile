# 1) Base image with Python
FROM python:3.11-slim

# 2) No Interactive Prompts: faster installs
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Set working directory
WORKDIR /app

# 4) Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 5) Copy app code
COPY . .

# 6) Expose and run with Uvicorn (Cloud Run listens on $PORT)
ENV PORT=8000
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
