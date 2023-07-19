FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update the package repositories and install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the project files to the container
COPY . /app

# Install the project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the entry point for the container
ENTRYPOINT [ "python3", "main.py" ]
