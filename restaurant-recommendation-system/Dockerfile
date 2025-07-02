# Use a more complete Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy everything to the working directory
COPY . .

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Railway will use
EXPOSE 5000

# Start the Flask app using gunicorn
CMD gunicorn api.app:app --bind 0.0.0.0:$PORT
