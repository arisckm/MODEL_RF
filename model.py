import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('rf_model.pkl')

# Streamlit UI
st.title("Water Quality Classification (RF)")
st.write("This app classifies whether a water sample is safe or not.")

# Take user input
pH = st.number_input("pH Level")
Hardness = st.number_input("Hardness")
Solids = st.number_input("Solids")
Chloramines = st.number_input("Chloramines")
Sulfate = st.number_input("Sulfate")
Conductivity = st.number_input("Conductivity")
Organic_carbon = st.number_input("Organic Carbon")
Trihalomethanes = st.number_input("Trihalomethanes")
Turbidity = st.number_input("Turbidity")

# Prediction
if st.button("Predict"):
    features = np.array([[pH, Hardness, Solids, Chloramines, Sulfate,
                          Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    prediction = model.predict(features)
    result = "Safe" if prediction[0] == 1 else "Not Safe"
    st.success(f"The water is: {result}")
