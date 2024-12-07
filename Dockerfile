# Sử dụng image Python chính thức làm base image
FROM python:3.9-slim
LABEL authors="Luke"

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép các file cần thiết vào container
COPY requirements.txt /app/

# Cài đặt các phụ thuộc từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . /app/

# Thiết lập biến môi trường PORT
ENV PORT=5000

# Mở cổng mà ứng dụng Flask sẽ chạy
EXPOSE $PORT

# Chạy ứng dụng Flask khi container khởi động
CMD ["python", "app.py", "--port=$PORT"]
