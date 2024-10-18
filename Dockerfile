FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y build-essential curl
ENV VIRTUAL_ENV=.venv \
    PATH="/opt/venv/bin:$PATH"

ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh
COPY . .
COPY .env /app/.env
WORKDIR /app
COPY ./requirements.lock .
COPY ./pyproject.toml .
RUN /root/.cargo/bin/uv venv /opt/venv && \
    /root/.cargo/bin/uv pip install --no-cache -r requirements.lock

CMD ["fastapi", "run"]
