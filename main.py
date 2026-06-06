import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIG & STYLING ---
st.set_page_config(
    page_title="Smart Savings Planner", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Dark Mode Settings */
    .stApp {
        background-color: #010409;
        color: #E2E8F0;
    }
    
    /* Sidebar Specific Styling */
    [data-testid="stSidebar"] {
        background-color: #0B0E14;
        border-right: 1px solid #21262D;
    }
    
    /* FIXED: Visibility of Headings in Sidebar */
    .stApp [data-testid="stSidebar"] .stMarkdown h2 {
        color: #10B981 !important; /* Green like main app headings */
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 700;
        font-size: 1.6rem !important;
        margin-top: -10px;
        margin-bottom: 5px;
    }

    .stApp [data-testid="stSidebar"] .stMarkdown h4 {
        color: #94A3B8 !important; /* Muted subtitle color */
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 500;
        font-size: 1.0rem !important;
        margin-top: -5px;
        margin-bottom: 20px;
    }

    /* Target inputs like text inputs and number inputs within sidebar */
    .stApp [data-testid="stSidebar"] .stNumberInput input,
    .stApp [data-testid="stSidebar"] .stTextInput input,
    .stApp [data-testid="stSidebar"] .stDateInput input,
    .stApp [data-testid="stSidebar"] .stSelectbox select {
        color: #10B981 !important; /* Bright, legible color */
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 6px;
    }

    /* FIX Labels within inputs */
    .stApp [data-testid="stSidebar"] label {
        color: #F0F6FC !important;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Global Headings */
    h1 {
        color: #10B981 !important; /* Accent Green */
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-weight: 600;
        font-size: 2.2rem !important;
    }
    
    h2 {
        color: #F8FAFC !important;
        font-size: 1.5rem !important;
        font-weight: 500;
    }
    
    h3 {
        color: #10B981 !important;
        font-size: 1.2rem !important;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Metrics Area */
    .metric-container {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }
    
    .metric-card {
        background-color: #0D1117;
        border-radius: 8px;
        padding: 20px;
        flex: 1;
        border: 1px solid #21262D;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .metric-label {
        color: #8B949E;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .metric-value {
        color: #10B981;
        font-size: 32px;
        font-weight: 700;
    }
    
    /* Global DIVIDER */
    hr {
        border-color: #21262D !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR SECTION ---
with st.sidebar:
    st.markdown("<h2>Smart Savings Planner</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Adham Awad</h4>", unsafe_allow_html=True) # --- FIX: Name added
    
    st.markdown("<h3>Financial Inputs</h3>", unsafe_allow_html=True)
    st.write("Configure your monthly parameters.")
    
    # User Inputs
    monthly_income = st.number_input("Monthly Income ($):", min_value=0.0, value=5000.0, step=100.0)
    savings_target_percentage = st.slider("Savings Target Percentage (%):", min_value=5, max_value=90, value=20)
    
    st.divider()
    st.markdown("<h3>Expenses breakdown</h3>", unsafe_allow_html=True)
    # Basic expenses inputs
    rent_expense = st.number_input("Rent / Housing ($):", min_value=0.0, value=1200.0)
    utilities_expense = st.number_input("Utilities & Bills ($):", min_value=0.0, value=300.0)
    food_expense = st.number_input("Groceries & Food ($):", min_value=0.0, value=500.0)
    other_expense = st.number_input("Other Expenses ($):", min_value=0.0, value=400.0)
    
    st.divider()
    st.write("App Status: Active ✅")

# --- 3. LOGIC SECTION ---
total_expenses = rent_expense + utilities_expense + food_expense + other_expense
savings_target_amount = monthly_income * (savings_target_percentage / 100)
net_remaining = monthly_income - total_expenses
surplus_deficit = net_remaining - savings_target_amount

# --- 4. MAIN CONTENT SECTION ---
st.markdown("<h1>💰 Monthly Financial Dashboard</h1>", unsafe_allow_html=True)
st.write("Review your progress and track your goals below.")
st.divider()

# --- Top metrics row ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Total Income</div><div class="metric-value">${monthly_income:,.2f}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Total Expenses</div><div class="metric-value" style="color: #EF4444;">-${total_expenses:,.2f}</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Savings Target</div><div class="metric-value">${savings_target_amount:,.2f}</div></div>', unsafe_allow_html=True)
with col4:
    color_goal = "#10B981" if net_remaining >= 0 else "#EF4444"
    st.markdown(f'<div class="metric-card"><div class="metric-label">Net Remaining</div><div class="metric-value" style="color: {color_goal};">${net_remaining:,.2f}</div></div>', unsafe_allow_html=True)

st.divider()

# --- Feedback row ---
st.markdown("<h2>Analysis & Recommendations</h2>", unsafe_allow_html=True)
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Expense breakdown chart")
    expense_dict = {
        'Category': ['Rent', 'Utilities', 'Food', 'Other'],
        'Amount ($)': [rent_expense, utilities_expense, food_expense, other_expense]
    }
    df_expenses = pd.DataFrame(expense_dict)
    st.bar_chart(df_expenses.set_index('Category'), color="#3B82F6")

with col_b:
    st.markdown("### Goal status")
    if surplus_deficit >= 0:
        st.success(f"Excellent! You've met your savings goal with a surplus of ${surplus_deficit:,.2f} this month.")
    elif net_remaining > 0:
        st.warning(f"You saved ${net_remaining:,.2f}, but fell short of your ${savings_target_amount:,.2f} goal by ${abs(surplus_deficit):,.2f}.")
    else:
        st.error(f"Alert! You spent more than you earned by ${abs(net_remaining):,.2f} this month.")

st.divider()
st.caption("Version 1.1 | Dev Adham Awad")