import streamlit as st
import pandas as pd

st.title("⚖ Welcome in BMI Calculator")

height = st.slider("Enter Your height (in cm): ", 100, 250, 175)
weight = st.slider("Enter your weight (in kg): ", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

# Show colored BMI result
if bmi < 18.5:
    color = "blue"
    category = "Underweight"
elif 18.5 <= bmi < 25:
    color = "green"
    category = "Normal weight"
elif 25 <= bmi < 30:
    color = "orange"
    category = "Overweight"
else:
    color = "red"
    category = "Obese"

st.markdown(f"### 🧮 Your BMI is: <span style='color:{color}; font-size:40px'>{bmi:.2f}</span>", unsafe_allow_html=True)
st.markdown(f"#### 💡 You are in the **{category}** category.", unsafe_allow_html=True)

# BMI Category Info
st.write("### 🔥----- BMI Categories -----🔥")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")
