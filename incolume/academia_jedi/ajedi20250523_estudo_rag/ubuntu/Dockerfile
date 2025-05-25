# Use the official Alpine image as the base image
FROM ubuntu:24.04

# Define the working directory
WORKDIR /code

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# The installer requires curl (and certificates) to download the release archive
# Run the installer then remove it
RUN apt update && apt install -y build-essential curl && sh /uv-installer.sh && rm /uv-installer.sh
# RUN uv sync --locked

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Informa ao Docker que o contêiner irá expor a porta informada
EXPOSE 8888

# run jupyter
CMD [ "uv", "run", "--with", "jupyter", "lab", "--no-browser"]
