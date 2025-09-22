# telco-churn-analysis
Customer churn prediction using ML, Streamlit, and Power BI
Full dataset at: https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data

# 📊 Telco Customer Churn Prediction

This project analyzes customer churn for a telecommunications company and builds an end-to-end machine learning pipeline to **predict churn**, **identify key risk drivers**, and provide **business-ready dashboards** for decision-making.  

---

## 🚀 Project Overview
Customer churn is a major challenge for subscription-based businesses. This project aims to:  
- Predict which customers are likely to churn  
- Identify high-risk, high-value customer segments  
- Quantify the financial impact of churn at different decision thresholds  
- Provide interactive dashboards for both **business users** and **data teams**

---

## 🛠️ Tech Stack
- **Python**: pandas, scikit-learn, XGBoost, LightGBM, SHAP, matplotlib, seaborn  
- **Streamlit**: Interactive ML app for exploring churn predictions  
- **Power BI**: Business-facing dashboard with KPIs & churn insights  

---

## 📂 Repository Structure
│
├── data/ # placeholder (dataset not uploaded)
│ └── README.md # instructions for dataset
│
├── src/ # Python scripts
│ ├── segment_analysis.py # customer segmentation analysis
│ ├── churn_train.py # ML pipeline (stacked model)
│ ├── streamlit_app.py # interactive dashboard app
│
├── dashboards/
│ └── churn_dashboard.pbix # Power BI dashboard
│
├── requirements.txt # dependencies
└── README.md # project documentation
