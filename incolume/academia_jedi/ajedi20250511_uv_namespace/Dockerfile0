FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /code

COPY <<EOF ./pyproject.toml
[project]
name = "example"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10,<4"
dependencies = ["cowsay"]
EOF

RUN uv lock
CMD ["python", "__init__.py"]
