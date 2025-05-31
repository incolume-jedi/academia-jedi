# Use the official Alpine image as the base image
FROM alpine:3.21

# Define the working directory
WORKDIR /code

# The installer requires curl (and certificates) to download the release archive
RUN apk add --no-cache curl ca-certificates gcc musl-dev linux-headers build-base cargo gcc git autoconf automake libffi-dev openssl-dev py-virtualenv

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# RUN uv sync --locked

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
