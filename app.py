import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")

st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Inputs
height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
weight = st.number_input("Weight (in kilograms)", min_value=10.0, max_value=300.0, value=70.0, step=0.5)

# BMI Calculation
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.subheader(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Normal weight")
    elif 25 <= bmi < 30:
        st.info("Overweight")
    else:
        st.error("Obese")
