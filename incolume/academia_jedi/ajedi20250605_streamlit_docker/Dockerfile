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

EXPOSE 8500-8599
