import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Thermal Expansion Calculator",
    page_icon="📏",
    layout="centered"
)

# Title
st.title("📏 Thermal Expansion Calculator")

st.write("Calculate linear thermal expansion of various materials.")

# Material Database
coefficients = {
    "Steel": 11.2e-6,
    "Stainless Steel": 17.3e-6,
    "Aluminium": 23.0e-6,
    "Cast Iron": 10.8e-6,
    "Copper": 16.5e-6
}

# Inputs
material = st.selectbox(
    "Select Material",
    list(coefficients.keys())
)

length = st.number_input(
    "Original Length (mm)",
    min_value=0.0,
    value=5000.0,
    step=100.0
)

delta_temp = st.number_input(
    "Temperature Difference (°C)",
    min_value=0.0,
    value=200.0,
    step=10.0
)

# Calculate Button
if st.button("Calculate Expansion"):

    alpha = coefficients[material]

    expansion = alpha * length * delta_temp

    st.success(f"Thermal Expansion = {expansion:.2f} mm")

    st.subheader("Calculation Summary")

    st.write(f"**Material:** {material}")
    st.write(f"**Original Length:** {length:,.2f} mm")
    st.write(f"**Temperature Difference:** {delta_temp:,.2f} °C")
    st.write(f"**Expansion:** {expansion:.2f} mm")