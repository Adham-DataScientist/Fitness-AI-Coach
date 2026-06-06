import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة بتصميم رياضي عريض (Soft Gym Dark Layout)
st.set_page_config(
    page_title="Fitness AI Coach & Workout Analytics", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص الـ CSS لإظهار النصوص البيضاء بوضوح وتنسيق الكروت والـ Sidebar
st.markdown("""
    <style>
    /* إعدادات الوضع الداكن الخلفية */
    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
    }
    
    /* تنسيق خاص بالشريط الجانبي (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #0B132B;
        border-right: 1px solid #1E293B;
    }
    
    /* تلوين وإظهار العناوين داخل الـ Sidebar بوضوح لمنع اللون الأبيض الباهت */
    .stApp [data-testid="stSidebar"] .stMarkdown h2 {
        color: #10B981 !important; /* أخضر رياضي واضح */
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 700;
        font-size: 1.6rem !important;
        margin-top: -10px;
        margin-bottom: 2px;
    }
    
    /* تنسيق اسمك تحت عنوان المشروع */
    .stApp [data-testid="stSidebar"] .stMarkdown h4 {
        color: #38BDF8 !important; /* لون أزرق مريح وهادئ للاسم */
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 600;
        font-size: 1.1rem !important;
        margin-top: -5px;
        margin-bottom: 20px;
    }

    .stApp [data-testid="stSidebar"] .stMarkdown h3 {
        color: #E2E8F0 !important;
        font-size: 1.2rem !important;
        font-weight: 600;
        margin-top: 15px;
    }

    /* تنسيق حقول الإدخال والقوائم داخل الـ Sidebar */
    .stApp [data-testid="stSidebar"] .stNumberInput input,
    .stApp [data-testid="stSidebar"] .stSelectbox select {
        color: #10B981 !important; 
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 6px;
    }

    .stApp [data-testid="stSidebar"] label {
        color: #F8FAFC !important;
        font-weight: 600;
    }
    
    /* العناوين الرئيسية في الصفحة */
    h1 {
        color: #10B981 !important; 
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 700;
        font-size: 2.2rem !important;
    }
    h2 {
        color: #F8FAFC !important;
        font-size: 1.4rem !important;
        font-weight: 500;
    }
    
    /* كروت عرض السعرات والماكروز */
    .macro-card {
        background-color: #1E293B;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #334155;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .macro-label {
        color: #94A3B8;
        font-size: 13px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    .macro-value {
        color: #10B981;
        font-size: 26px;
        font-weight: 700;
    }
    
    /* حاويات الجداول والرسومات */
    .workout-box {
        background-color: #1E293B;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }
    .coach-tip {
        background-color: #1E293B; 
        padding: 15px; 
        border-radius: 8px; 
        border-left: 4px solid #38BDF8;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الشريط الجانبي الذكي للمدخلات البدنية (Sidebar)
with st.sidebar:
    st.markdown("<h2>Fitness AI Coach</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Adham Awad</h4>", unsafe_allow_html=True) # --- إضافة اسمك هنا بوضوح
    
    st.markdown("<h3>Athlete Metrics</h3>", unsafe_allow_html=True)
    st.write("Input your physical attributes & goals.")
    st.divider()
    
    # مدخلات المستخدم البدنية
    weight = st.number_input("Current Weight (kg):", min_value=30.0, max_value=200.0, value=80.0, step=0.5)
    height = st.number_input("Current Height (cm):", min_value=100.0, max_value=250.0, value=175.0, step=1.0)
    age = st.number_input("Age:", min_value=10, max_value=100, value=25)
    
    gender = st.radio("Gender:", ["Male", "Female"], horizontal=True)
    
    st.divider()
    fitness_goal = st.selectbox(
        "Select Fitness Goal:",
        ["Cut & Fat Loss (تنشيف)", "Clean Bulk (تضخيم عضل)", "Maintenance (ثبات وزن)"]
    )
    
    st.divider()
    st.markdown("🔹 **Coach Status:** `AI-Active`")

# الحسابات الرياضية الذكية (Fitness Algorithmic Engine)
if gender == "Male":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

if "Fat Loss" in fitness_goal:
    target_calories = bmr * 1.375 - 500  
    protein_g = weight * 2.2
    carbs_g = weight * 2.0
    fats_g = weight * 0.8
elif "Bulk" in fitness_goal:
    target_calories = bmr * 1.375 + 400  
    protein_g = weight * 2.0
    carbs_g = weight * 4.0
    fats_g = weight * 1.0
else:
    target_calories = bmr * 1.375        
    protein_g = weight * 1.8
    carbs_g = weight * 3.0
    fats_g = weight * 0.9

# 3. الصفحة الرئيسية (Main Dashboard Screen)
st.markdown("<h1>🏋️‍♂️ Fitness AI Coach & Workout Analytics</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #94A3B8; font-size: 14px; margin-top: -10px;'>Your dynamic, algorithmic dashboard for personalized macronutrient splitting and training workflows.</p>", unsafe_allow_html=True)
st.divider()

# --- كروت الـ Macros العلوية ---
st.markdown("<h2>🎯 Daily Target Macronutrients</h2>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'<div class="macro-card"><div class="macro-label">Target Calories</div><div class="macro-value">{int(target_calories)} kcal</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="macro-card"><div class="macro-label">Protein Target</div><div class="macro-value" style="color: #38BDF8;">{int(protein_g)}g</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="macro-card"><div class="macro-label">Carbohydrates</div><div class="macro-value" style="color: #F59E0B;">{int(carbs_g)}g</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="macro-card"><div class="macro-label">Healthy Fats</div><div class="macro-value" style="color: #EF4444;">{int(fats_g)}g</div></div>', unsafe_allow_html=True)

st.divider()

# --- قسم الجداول والرسومات التحليلية ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="workout-box">', unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 14px; font-weight: 500; margin-bottom: 15px;'>💪 Recommended AI Workout Split</p>", unsafe_allow_html=True)
    
    if "Fat Loss" in fitness_goal:
        split_data = pd.DataFrame({
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'Workout Type': ['Push (Chest/Shoulders/Triceps)', 'Pull (Back/Biceps)', 'Legs & Abs', 'HIIT Cardio + Core', 'Full Body Mobility'],
            'Duration': ['45 mins', '45 mins', '50 mins', '30 mins', '40 mins']
        }).set_index('Day')
    else:
        split_data = pd.DataFrame({
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'Workout Type': ['Heavy Upper Body', 'Heavy Lower Body', 'Rest / Active Recovery', 'Hypertrophy Push', 'Hypertrophy Pull'],
            'Duration': ['60 mins', '60 mins', 'Rest', '55 mins', '55 mins']
        }).set_index('Day')
        
    st.dataframe(split_data, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="workout-box">', unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 14px; font-weight: 500; margin-bottom: 15px;'>📈 6-Week Weight Projection Trend</p>", unsafe_allow_html=True)
    
    weeks = [f"Week {i}" for i in range(1, 7)]
    if "Fat Loss" in fitness_goal:
        weight_trend = [weight - (i * 0.5) for i in range(6)]  
    elif "Bulk" in fitness_goal:
        weight_trend = [weight + (i * 0.3) for i in range(6)]  
    else:
        weight_trend = [weight] * 6
        
    trend_df = pd.DataFrame({
        'Timeline': weeks,
        'Projected Weight (kg)': weight_trend
    }).set_index('Timeline')
    
    st.line_chart(trend_df, color="#10B981", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- قسم نصائح الكوتش الذكي ---
st.divider()
st.markdown("<h2>🤖 AI Coach Strategic Insights</h2>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="coach-tip">
        <span style='color: #A7F3D0;'>💡 <b>Personalized Coach Tip:</b> Based on your goal <b>({fitness_goal})</b>, ensure you consume at least 3-4 liters of water daily to optimize natural metabolic performance parameters.</span>
    </div>
    """, 
    unsafe_allow_html=True
)