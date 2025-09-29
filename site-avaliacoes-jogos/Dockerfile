# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install dependencies.
# We copy requirements.txt first to leverage Docker's layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY ./AvaliacoesSite .

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]