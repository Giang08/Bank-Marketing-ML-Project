# Sử dụng môi trường Python gọn nhẹ
FROM python:3.9-slim

# Đặt thư mục làm việc trong Docker
WORKDIR /app

# Copy file requirements và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code frontend vào
COPY ./frontend /app/frontend

# Lệnh chạy Streamlit khi khởi động
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]