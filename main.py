import streamlit as st
import pandas as pd

# --- العنوان ---
st.title("🍎 Fitness AI Coach")
st.subheader("احسب صحتك بذكاء")

# --- المدخلات (الـ Widgets) ---
# سطر واحد فيه عمودين
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("الوزن (كيلوجرام)", min_value=30.0, max_value=200.0, value=70.0)
    age = st.slider("العمر", 10, 100, 25)

with col2:
    height = st.number_input("الطول (سنتيمتر)", min_value=100.0, max_value=250.0, value=170.0)
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

# زر الحساب
if st.button("احسب النتائج 🚀"):
    # تحويل الطول لمتر
    height_m = height / 100
    # معادلة الـ BMI
    bmi = weight / (height_m ** 2)
    
    st.divider()
    
    # عرض النتيجة بشكل شيك
    st.metric("مؤشر كتلة جسمك (BMI)", f"{bmi:.1f}")
    
    if bmi < 18.5:
        st.warning("وزنك أقل من الطبيعي")
    elif 18.5 <= bmi < 25:
        st.success("وزنك مثالي! استمر")
    else:
        st.error("تحتاج لتقليل الوزن")