# 📦 Walmart Supply Chain & Demand Intelligence Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR-STREAMLIT-URL-HERE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end machine learning and data analytics application designed to forecast weekly store revenues, analyze macroeconomic indicators, and optimize inventory logistics for retail supply chain management using a high-accuracy **Random Forest Regressor ($R^2 = 0.9589$)**.

---

## 🚀 Live Demo
Experience the interactive web application live in your browser:  
👉 **[View Live Streamlit App](https://walmart-predictive-supplychain-23o9nygakgntd57tcartsy.streamlit.app/)**

---

## 📸 Dashboard Preview

### 1. Overview & Real-Time Predictions
The main interface allows stakeholders to input store parameters, adjust macroeconomic factors (Temperature, Fuel Price, CPI, Unemployment), and instantly generate revenue predictions alongside strategic operational recommendations.

![Dashboard Top View](https://raw.githubusercontent.com/shabbirrajgarh/walmart-predictive-supplychain/main/assets/dashboard_top.png)

### 2. Feature Importance & Explainability
Detailed breakdown of key feature influencers (such as Store ID, CPI, and Fuel Price) driving model predictions, ensuring transparent and data-backed supply chain decisions.

![Dashboard Bottom View](https://raw.githubusercontent.com/shabbirrajgarh/walmart-predictive-supplychain/main/assets/dashboard_bottom.png)
---

## 🛠️ Key Features
* **Predictive Analytics:** Powered by a tuned Random Forest model delivering robust forecasting performance ($R^2 = 0.9589$).
* **Dynamic Scenario Testing:** Real-time sliders for macroeconomic indicators (CPI, Unemployment, Fuel Prices) to simulate market shifts.
* **Automated Recommendations:** Context-aware suggestions for inventory buffering, logistics routing, and seasonal staffing based on predicted demand surges.
* **Exploratory Data Analysis (EDA):** Deep dive notebooks covering data cleaning, feature engineering, and supply chain insights.

---

## 📂 Project Structure
```text
walmart-predictive-supplychain/
│
├── assets/                  # UI screenshots and visual assets
├── notebooks/               # Jupyter notebooks for EDA and Model Training
│   ├── 01_data_cleaning_features.ipynb
│   ├── 02_eda_supply_chain_insights.ipynb
│   └── 03_model_training_evaluation.ipynb
│
├── app.py                   # Streamlit interactive web application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
