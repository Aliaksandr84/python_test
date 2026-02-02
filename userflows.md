# User Flows

# 1\. Run Data Quality Checker Locally

# Clone the Repository:

# 

# bash

# 

# Copy

# Download

# git clone https://github.com/Aliaksandr84/python\_test.git

# cd python\_test

# Install Dependencies:

# 

# bash

# 

# Copy

# Download

# pip install -r requirements.txt

# Configure Input Data:

# 

# Place or update your CSV file (e.g., sample.csv) in the repo root.

# 

# Adjust columns or config as needed.

# 

# Run the Application:

# 

# bash

# 

# Copy

# Download

# python main.py

# The script will load the CSV, check the configured columns for nulls, and output a formatted report to the console.

# 

# If configured, an HTML report (report.html) or email notification is also produced.

# 

# 2\. View Data Quality Report in Browser (If Enabled)

# After running the main script, open report.html in your browser.

# 

# Optional: If using a Flask app, run and visit http://localhost:5000.

# 

# 3\. Run Tests

# From the project root, execute:

# 

# bash

# 

# Copy

# Download

# pytest

# or, for a single file:

# 

# bash

# 

# Copy

# Download

# pytest test\_checker.py

# 4\. Change Configuration

# Update the YAML file in the configs/ folder to change columns to check or other settings.

# 

# Alternatively, adjust constants at the top of main.py.

# 

# 5\. Add a New Data Source or Check

# Add your new checker function to the appropriate module (e.g., data\_quality/checker.py).

# 

# Import and call it from main.py or another orchestrator.

# 

# Add or update test files to cover new behavior.

