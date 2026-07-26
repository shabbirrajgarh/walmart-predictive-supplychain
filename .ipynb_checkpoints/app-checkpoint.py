import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# Set Page Config
st.set_page_config(
    page_title="Walmart Supply Chain Intelligence Dashboard",
    page_icon="📦",
    layout="wide"
)

# Load Model
@st.cache_resource
def load_model():
    return joblib.load('models/walmart_rf_model.pkl')

model = load_model()

# Title Header
st.title("📦 Walmart Supply Chain & Demand Intelligence Dashboard")
st.markdown("""
Predict weekly revenue, analyze macroeconomic factors, and optimize inventory allocation using a high-accuracy **Random Forest Regressor** ($R^2 = 0.9589$).
""")

st.divider()

# Sidebar Setup
st.sidebar.header("🔧 Demand Drivers & Parameters")

store = st.sidebar.number_input("Store ID", min_value=1, max_value=45, value=12)
holiday_flag = st.sidebar.selectbox("Holiday Week?", [0, 1], format_func=lambda x: "Yes (Surge Expected)" if x == 1 else "No (Standard Week)")
temperature = st.sidebar.slider("Temperature (°F)", min_value=0.0, max_value=110.0, value=50.1)
fuel_price = st.sidebar.slider("Fuel Price ($)", min_value=2.0, max_value=5.0, value=3.5)
cpi = st.sidebar.slider("CPI (Consumer Price Index)", min_value=120.0, max_value=230.0, value=142.5)
unemployment = st.sidebar.slider("Unemployment Rate (%)", min_value=3.0, max_value=15.0, value=5.5)

selected_date = st.sidebar.date_input("Select Forecast Target Date")
year = selected_date.year
month = selected_date.month
week_of_year = selected_date.isocalendar()[1]
day_of_week = selected_date.weekday()

is_extreme_cold = 1 if temperature < 32 else 0
is_extreme_heat = 1 if temperature > 85 else 0

# Inference
input_data = pd.DataFrame([[
    store, holiday_flag, temperature, fuel_price, cpi,
    unemployment, year, month, week_of_year, day_of_week,
    is_extreme_cold, is_extreme_heat
]], columns=[
    'Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI',
    'Unemployment', 'Year', 'Month', 'WeekOfYear', 'DayOfWeek',
    'Is_Extreme_Cold', 'Is_Extreme_Heat'
])

prediction = model.predict(input_data)[0]

# --- MAIN DASHBOARD BODY ---

# Top Metric Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Predicted Weekly Revenue", value=f"${prediction:,.2f}")

with col2:
    status = "🔥 Holiday Spike (+13.15%)" if holiday_flag == 1 else "📦 Normal Demand"
    st.metric(label="Operational Regime", value=status)

with col3:
    st.metric(label="Consumer Index (CPI)", value=f"{cpi:.1f}")

with col4:
    st.metric(label="Unemployment Impact", value=f"{unemployment:.1f}%")

st.divider()

# Charts Section
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Key Feature Influencers")
    feature_names = ['Store ID', 'CPI', 'Unemployment', 'Week of Year', 'Temperature', 'Fuel Price']
    importance_values = [0.66, 0.15, 0.10, 0.05, 0.02, 0.02]
    
    fig_imp = px.bar(
        x=importance_values, 
        y=feature_names, 
        orientation='h',
        labels={'x': 'Impact Weight', 'y': 'Feature'},
        color=importance_values,
        color_continuous_scale='Viridis'
    )
    fig_imp.update_layout(showlegend=False, height=320, margin=dict(l=0, r=0, t=20, b=0))
    st.plotly_chart(fig_imp, use_container_width=True)

with col_right:
    st.subheader("💡 Strategic Supply Chain Recommendations")
    if holiday_flag == 1:
        st.success("""
        * **Inventory Buffering:** Increase safety stock by **15-20%** for Store #{} to handle holiday traffic.
        * **Logistics Routing:** Pre-book third-party carrier capacity 2 weeks in advance.
        * **Staffing:** Increase seasonal floor workforce to mitigate stockout risks.
        """.format(store))
    else:
        st.info("""
        * **Standard Replenishment:** Maintain normal automated reorder points for Store #{}.
        * **Cost Optimization:** Consolidate regional shipments to minimize transport fuel costs.
        * **Local Sensitivity:** Monitor CPI variations for localized discounting strategy.
        """.format(store))

st.caption("Model Version: 1.0.0 | Random Forest Regressor | Baseline Evaluation R²: 0.9589")