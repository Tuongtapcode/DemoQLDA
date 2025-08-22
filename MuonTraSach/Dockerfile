# Dùng Python base image
FROM python:3.10-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt requirements.txt

# Cài thư viện cần thiết
RUN pip install -r requirements.txt

# Copy toàn bộ source code (thư mục MuonTraSach) vào container
COPY MuonTraSach .

# Chạy app khi container khởi động
CMD ["python", "index.py"]
