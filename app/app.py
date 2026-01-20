import os
import streamlit as st
import pickle
import numpy as np

# Get base directory (houseprediction)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model safely
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict the price")

gr_liv_area = st.number_input("Living Area (sq ft)", min_value=300)
overall_qual = st.slider("Overall Quality (1–10)", 1, 10)
total_bsmt = st.number_input("Basement Area (sq ft)", min_value=0)

if st.button("Predict Price"):
    input_data = np.array([[gr_liv_area, overall_qual, total_bsmt]])
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
