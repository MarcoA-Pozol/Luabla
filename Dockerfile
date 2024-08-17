# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code/Luabla

# Copy the requirements file into the container at /code/Luabla
COPY requirements.txt /code/Luabla/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /code/Luabla
COPY . /code/

# Make port 8700 available to the world outside this container
EXPOSE 8700

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8700"]
