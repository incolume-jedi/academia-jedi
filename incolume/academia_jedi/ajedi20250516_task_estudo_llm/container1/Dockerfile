# System base
FROM alpine:3.21

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Download the latest installer for uv
COPY --from=ghcr.io/astral-sh/uv:python3.13-alpine /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/

# The installer requires curl, Run the uv installer then remove it
RUN apk update; apk add --no-cache build-base; uv venv /opt/python3.13 -p 3.13
