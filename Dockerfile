FROM python:3.11

# Copy in your requirements file
COPY requirements.txt /requirements.txt

# Install your requirements
RUN pip install -r /requirements.txt

# Copy your source code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Run your application
ENTRYPOINT ["python", "/app/entrypoint.py"]
