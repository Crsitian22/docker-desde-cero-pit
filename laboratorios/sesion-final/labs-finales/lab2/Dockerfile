FROM python:3.11-slim

LABEL maintainer="astra@uni.edu.pe"
LABEL description="Gestor de Tareas - Docker Labs UNI"
LABEL version="1.0"

ARG APP_PORT=5000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=${APP_PORT}

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
