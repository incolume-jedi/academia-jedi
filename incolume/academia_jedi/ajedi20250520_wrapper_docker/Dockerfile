FROM ghcr.io/astral-sh/uv:python3.13-alpine
# USER 1000:1000
WORKDIR /code
COPY ./pyproject.toml .
COPY ./src .
RUN uv sync
CMD ["uv", "run", "ajedi20250520-wrapper-docker"]
