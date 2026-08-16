FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --upgrade pip \
    && pip install .

COPY . .

RUN mkdir -p \
    allure-results \
    allure-report \
    screenshots \
    downloads \
    logs

CMD ["pytest"]