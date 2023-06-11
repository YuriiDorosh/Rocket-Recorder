# We use the official Python image as the base image
FROM python:3.9

# We set project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . /app
WORKDIR /app

# We run the command when the container starts
CMD ["python", "__main__.py"]
