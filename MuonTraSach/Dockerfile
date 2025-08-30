# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code (cả thư mục MuonTraSach con)
COPY MuonTraSach ./MuonTraSach

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "MuonTraSach/index.py"]
