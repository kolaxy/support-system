FROM python:3.11.5-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./app/poetry.lock ./app/pyproject.toml /
COPY ./app/scripts /scripts

COPY ./app /app

RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev

RUN adduser --disabled-password --gecos '' dockuser && \
    chmod -R 755 /app && \
    chmod -R +x /scripts

WORKDIR /app

EXPOSE 8000

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]
