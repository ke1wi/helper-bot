FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl && \
    rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod +x /install.sh && /install.sh && rm /install.sh

COPY ./requirements.lock /app/requirements.lock
COPY ./pyproject.toml /app/pyproject.toml
WORKDIR /app

RUN /root/.cargo/bin/uv venv $VIRTUAL_ENV && \
    /root/.cargo/bin/uv pip install --no-cache-dir -r requirements.lock

COPY . .

COPY .env /app/.env

WORKDIR /app

CMD ["fastapi", "run"]
