# We use the official Python image as the base image
FROM python:3.10.6

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Set project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . /app
WORKDIR /app

# We run the command when the container starts
CMD ["python", "__main__.py"]
