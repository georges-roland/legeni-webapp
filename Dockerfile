FROM python:3.12-slim AS base
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

FROM base AS test
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
COPY test_app.py .
RUN flake8 . && pytest

FROM base AS prod
ARG APP_VERSION=1.0.0
ENV APP_VERSION=${APP_VERSION} \
    APP_ENV=prod \
    APP_COLOR=#1f6feb \
    PORT=5000
EXPOSE 5000
CMD ["python", "app.py"]
