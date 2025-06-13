# Dockerfile otimized for project manager uv
# Exposed ports range: 8080-8599
# This Dockerfile sets up a minimal environment for the uv project manager

# Use the official Alpine image as the base image
FROM alpine:3.21

# Define the working directory
WORKDIR /code

# Copy the requirements file into the container
# COPY ./requirements.txt ./

# The installer requires curl (and certificates) to download the release archive
# RUN apk add --no-cache ca-certificates gcc musl-dev linux-headers build-base libffi-dev openssl-dev git

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:${PATH}"

EXPOSE 8080-8599
