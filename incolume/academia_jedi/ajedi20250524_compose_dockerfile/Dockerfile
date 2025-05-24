# Arguments to specify for this image
ARG ALPINE_TAG=3.21

# Use the official Alpine image as the base image
FROM alpine:${ALPINE_TAG:-3.21}

# Define the working directory
WORKDIR /code

# The installer requires curl (and certificates) to download the release archive
RUN apk add --no-cache curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
