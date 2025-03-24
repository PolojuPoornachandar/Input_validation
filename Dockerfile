# Step 1: Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to install dependencies
COPY requirements.txt /app/

# Step 4: Copy the rest of your application code to the container
COPY . /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose the port for the application (for future use if needed)
EXPOSE 5000

# Step 7: Command to run the test suite
CMD ["python", "-m", "unittest", "discover"]

