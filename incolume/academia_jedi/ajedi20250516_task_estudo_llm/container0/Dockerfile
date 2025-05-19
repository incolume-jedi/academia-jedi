# System base
FROM alpine:3.21

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Download the latest installer for uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# The installer requires curl, Run the uv installer then remove it
RUN apk update; apk add --no-cache build-base curl && sh /uv-installer.sh; rm /uv-installer.sh; uv venv /opt/python3.13 -p 3.13.2
