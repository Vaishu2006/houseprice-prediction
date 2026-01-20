# 🏠 House Price Prediction – Machine Learning Web App

An end-to-end Machine Learning project that predicts house prices using housing features.
The trained ML model is deployed as an interactive web application using Streamlit.

---

## 📌 Project Overview
This project demonstrates the complete Machine Learning lifecycle:
- Data analysis (EDA)
- Feature selection
- Model training & evaluation
- Model saving
- Web app deployment

---

## 📊 Dataset
- Source: Kaggle – House Prices: Advanced Regression Techniques
- Target Variable: SalePrice

### Features Used
- GrLivArea – Living area (sq ft)
- OverallQual – Overall quality (1–10)
- TotalBsmtSF – Basement area (sq ft)

---

## ⚙️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Git & GitHub

---

## 🧠 ML Workflow
1. Exploratory Data Analysis (EDA)
2. Feature selection
3. Model training (Linear Regression)
4. Model evaluation (R² ≈ 0.78)
5. Model persistence (Pickle)
6. Streamlit web app

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Vaishu2006/houseprice-prediction.git
cd houseprice-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/train_model.py
streamlit run app/app.py

## 🔗 Live Demo
👉 https://houseprice-prediction-xywbb2xlwus5vda6o9nbhv.streamlit.app/


