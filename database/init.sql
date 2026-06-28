-- Tạo database nếu chưa có
CREATE DATABASE IF NOT EXISTS bank_marketing_db;
USE bank_marketing_db;

-- Tạo bảng lưu lịch sử dự đoán (Tuyệt đối không có cột duration)
CREATE TABLE IF NOT EXISTS prediction_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    job VARCHAR(50),
    marital VARCHAR(50),
    education VARCHAR(50),
    prediction_result VARCHAR(10),
    probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);