
# app/Dockerfile - Build production-ready Docker image for Python app

# Use official Python slim image for minimal footprint
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies securely
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Set environment variables for production
ENV FLASK_ENV=production

# Expose port 8080
EXPOSE 8080

# Run application as non-root user for security
USER 1001

# Command to start the application
CMD ["python", "app.py"]