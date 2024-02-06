FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

