# 📦 Walmart Predictive Supply Chain & Demand Intelligence

An end-to-end Machine Learning pipeline and interactive executive dashboard built to forecast weekly store-level demand, analyze macroeconomic sensitivity, and optimize supply chain allocation for retail operations.

---

## 🎯 Executive Summary & Impact

* **High-Accuracy Demand Model:** Trained a **Random Forest Regressor** achieving an **$R^2$ score of 0.9589** (~96% variance explained).
* **Operational Demand Lift:** Identified a statistically significant **+13.15% surge** in weekly sales during major holiday events.
* **Interactive Frontend:** Built and deployed a real-time **Streamlit Web Application** for interactive demand simulation and inventory buffer recommendations.

---

## 📁 Repository Architecture

```text
walmart-predictive-supplychain/
├── data/
│   ├── raw/                      # Raw Walmart sales data
│   └── processed/                # Cleaned data with engineered features
├── models/
│   └── walmart_rf_model.pkl      # Serialized trained Random Forest model
├── notebooks/
│   ├── 01_data_cleaning_features.ipynb
│   ├── 02_eda_supply_chain_insights.ipynb
│   └── 03_model_training_evaluation.ipynb
├── app.py                        # Streamlit Executive Dashboard
├── requirements.txt              # Project dependencies
└── README.md                     # Documentation
