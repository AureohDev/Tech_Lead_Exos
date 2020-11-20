# Use the official image as a parent image.
FROM ubuntu:20.04
#FROM python:3.8

# Set the working directory.
WORKDIR /usr/src/app

# Install on ubuntu python3.7, python3-pip, and Vim
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.7 \
    python3-pip \
    vim \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt in filesystem working directory
COPY requirements.txt .

# Install with pip3 all python lib from requirements
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# copy all files from current directory to filesystem working directory.
COPY . .

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 80

# Run the specified command within the container.
# Here is launch of app.py with python 3
CMD ["python3","app.py"]
