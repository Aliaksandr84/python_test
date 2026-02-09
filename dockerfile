# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements first, then rest to leverage docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all code
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Environment variable to tell Flask to run in production mode
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Command to run app
# If you use Flask's app.py: `flask run --host=0.0.0.0 --port=5000`
# If you use main.py with: if __name__ == '__main__': app.run()
CMD ["python", "main.py"]