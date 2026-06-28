from fastapi import FastAPI

# Khởi tạo ứng dụng FastAPI
app = FastAPI(title="Bank Marketing Prediction API", version="1.0")

# 1. Endpoint kiểm tra sức khỏe hệ thống
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API đang hoạt động trơn tru!"}

# 2. Endpoint thông tin mô hình (Có cấu hình hiển thị dùng SMOTE theo yêu cầu)
@app.get("/model-info")
def model_info():
    return {
        "model_name": "Bank Marketing Classifier",
        "version": "1.0",
        "smote_used": True,
        "description": "Mô hình dùng SMOTE training"
    }

# 3. Endpoint dự đoán (Tạm thời trả về kết quả giả/dummy, sau này sẽ ghép model thật vào)
@app.post("/predict")
def predict():
    return {
        "status": "success",
        "prediction": "yes", 
        "probability": 0.85
    }

# 4. Endpoint xem lịch sử (Tạm thời để trống, sau này sẽ nối với Database)
@app.get("/history")
def get_history():
    return {"message": "Đây sẽ là nơi trả về dữ liệu từ Database MySQL/PostgreSQL"}