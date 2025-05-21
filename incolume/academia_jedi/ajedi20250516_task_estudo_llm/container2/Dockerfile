FROM ghcr.io/astral-sh/uv:python3.13-alpine
WORKDIR /code
COPY ./pyproject.toml .
RUN uv venv -p 3.13; source .venv/bin/activate; python -V
