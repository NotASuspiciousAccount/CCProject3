FROM python:3.9-alpine

# Set the working directory
WORKDIR /home/data

# Copy Python script and text files to the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create output directory, install dependencies, and run the script
RUN mkdir /home/data/output
RUN pip install contractions
RUN python3 script.py

# Print results to terminal
WORKDIR /home/data/output
CMD ["cat", "result.txt"]