# Sử dụng môi trường Python gọn nhẹ
FROM python:3.9-slim

# Đặt thư mục làm việc trong Docker
WORKDIR /app

# Copy file requirements và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code backend vào
COPY ./backend /app/backend

# Lệnh chạy API khi khởi động
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]