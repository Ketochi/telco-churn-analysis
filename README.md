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


---

## 📊 Data
Dataset: [Telco Customer Churn (Kaggle)](https://www.kaggle.com/blastchar/telco-customer-churn)  

- **Customers**: ~7,000  
- **Features**: demographics, account information, contract type, services used  
- **Target**: `Churn` (Yes/No)  

⚠️ Dataset is not included in this repo.  
To run locally, download it from Kaggle and place in the `data/` folder.  

---

## 🔎 Methodology
1. **Data Preprocessing**  
   - Handling missing values  
   - Encoding categorical features  
   - Scaling numerical features  

2. **Exploratory Data Analysis (EDA)**  
   - Segmenting customers by contract type, tenure, PaymentMethod  
   - Identifying churn-prone groups  

3. **Machine Learning Pipeline**  
   - Models: RandomForest, XGBoost, LightGBM, SVM  
   - Combined using **Stacked Ensemble**  
   - Evaluation: Accuracy, Precision-Recall AUC, Lift curves, Cost-Benefit  

4. **Model Explainability**  
   - SHAP values for feature importance  
   - Business insights from top churn drivers  

5. **Decision Threshold Optimization**  
   - Profit maximized at ~4% threshold  
   - Lower thresholds → more customer-centric, higher retention costs  
   - Higher thresholds → cost-efficient, but risk losing valuable customers  

---

## 📈 Business Insights
- **Month-to-month contracts** have the highest churn risk  
- **Electronic check payment method** strongly linked to churn  
- **Tenure**: long-term customers are far less likely to churn  
- Balancing **profit vs. retention strategy** depends on threshold selection  

---

## 📊 Dashboards
- **Streamlit App**: interactive churn prediction & threshold tuning  
- **Power BI Dashboard**: high-level KPIs, segment analysis, and churn drivers  

*(Screenshots coming soon)*  

---

## ⚡ How to Run
Clone the repo and install dependencies:

To run streamlit use 
streamlit run src/streamlit_app.py # If you are running locally replace src/streamlit_app.py with file path

```bash
pip install -r requirements.txt



