import streamlit as st
import requests

# Cấu hình trang web
st.set_page_config(page_title="Bank Marketing Prediction", layout="wide")

# Tạo thanh menu bên trái (Sidebar)
st.sidebar.title("Điều hướng")
menu = ["Dashboard", "Predict", "Model Info", "History", "Batch"]
choice = st.sidebar.selectbox("Chọn màn hình", menu)

# --- 1. MÀN HÌNH DASHBOARD ---
if choice == "Dashboard":
    st.title("📊 Trang chủ / Dashboard")
    st.write("Chào mừng đến với hệ thống dự đoán khách hàng đăng ký gửi tiết kiệm có kỳ hạn (Bank Marketing).")
    st.info("Hệ thống sẽ giúp dự đoán xem một khách hàng có đồng ý gửi tiết kiệm hay không dựa trên thông tin cá nhân và chiến dịch marketing.")

# --- 2. MÀN HÌNH PREDICT ---
elif choice == "Predict":
    st.title("🎯 Màn hình Dự đoán (Predict)")
    st.warning("Mô hình dùng SMOTE training") # Yêu cầu bắt buộc của Leader
    
    st.write("Vui lòng nhập thông tin khách hàng:")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Tuổi (Age)", min_value=18, max_value=100, value=30)
        job = st.selectbox("Nghề nghiệp (Job)", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
    with col2:
        marital = st.selectbox("Tình trạng hôn nhân (Marital)", ["married", "single", "divorced"])
        education = st.selectbox("Học vấn (Education)", ["primary", "secondary", "tertiary", "unknown"])
        
    if st.button("Dự đoán ngay"):
        # Gọi sang API Backend của bạn để lấy kết quả
        try:
            res = requests.post("http://127.0.0.1:8000/predict")
            if res.status_code == 200:
                data = res.json()
                st.success(f"Kết quả dự đoán: Khách hàng sẽ phản hồi **{data['prediction'].upper()}**")
                st.info(f"Độ tin cậy (Xác suất): {data['probability'] * 100}%")
        except:
            st.error("Lỗi kết nối! Hãy đảm bảo bạn chưa tắt Terminal chạy FastAPI nhé.")

# --- 3. MÀN HÌNH MODEL INFO ---
elif choice == "Model Info":
    st.title("🤖 Thông tin Mô hình (Model Info)")
    try:
        res = requests.get("http://127.0.0.1:8000/model-info")
        if res.status_code == 200:
            st.json(res.json())
    except:
         st.error("Lỗi kết nối đến API.")

# --- 4. MÀN HÌNH HISTORY ---
elif choice == "History":
    st.title("🕰️ Lịch sử Dự đoán (History)")
    st.write("Dữ liệu lịch sử sẽ được truy vấn từ Database (MySQL/PostgreSQL) và hiển thị thành bảng tại đây.")

# --- 5. MÀN HÌNH BATCH PREDICTION ---
elif choice == "Batch":
    st.title("📁 Dự đoán hàng loạt (Batch Prediction)")
    uploaded_file = st.file_uploader("Tải lên file CSV chứa danh sách khách hàng", type=["csv"])
    if uploaded_file is not None:
        st.write("Đã nhận file. Sẵn sàng dự đoán!")
        st.button("Chạy dự đoán hàng loạt")