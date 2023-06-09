# Base image
FROM python:3.10-slim

RUN useradd flaskapp

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

RUN chmod +x boot.sh
RUN chown -R flaskapp:flaskapp ./
USER flaskapp

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["./boot.sh"]
